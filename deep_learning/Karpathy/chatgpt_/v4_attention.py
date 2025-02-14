#### My janky single head attention

import torch
import torch.nn as nn
from torch.nn import functional as F
from pdb import set_trace as bp
import matplotlib.pyplot as plt

#function to view and plot a tensor
def view(x):
    #x is a pytorch tensor
    x = x.to("cpu").detach().numpy()
    plt.imshow(x)
    plt.pause(1)

# hyperparameters
batch_size = 32 #number of independent sequences
block_size = 8  #maximum context length of our prediciton \
# (in reality only the last element is used for the bigram model)
head_size = 16
n_embd = 32 # number of embedding demensions
max_iters = 100000
eval_interval = 300
learing_rate = 1e-2
device = "cuda" if torch.cuda.is_available() else "cpu"
eval_iters = 200
#-------------------------------------

torch.manual_seed(1337)

#curl -o input.txt https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
with open("input.txt", 'r', encoding = 'utf-8') as f:
    text = f.read()

#extract unique characters
chars = sorted(list(set(text))) 
vocab_size = len(chars)
# create a mapping from c -> i and vice versa
itos = {i:char for i,char in enumerate(chars)}
stoi = {char:i for i,char in itos.items()}
#encoder and decode
encode = lambda s: [stoi[c] for c in s] 
decode = lambda l: "".join([itos[i] for i in l])

#Train and test splits
data = torch.tensor(encode(text), dtype = torch.long)
n = int(0.9 * len(data))
train_data = data[:n]
val_data = data[n:]

#data loading
def get_batch(split):
    #samples random locations in the dataset to pull chunk
    data = train_data if split == "train" else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,)) #size argument must be a tuple
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    x, y = x.to(device), y.to(device)
    return x, y

@torch.no_grad() #context manager
def estimate_loss():
    out = {}
    model.eval() #set model to evaluation phase - this doesnt do anything for our simple bigram but is important when working with models with drop out adn bacth norms layers etc.
    for split in ["train","val"]:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            X, Y = get_batch(split)
            logits, loss = model(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out

class BigramLanguageModel(nn.Module):
    def __init__(self):
        super().__init__()
        # we want to complicate the model not - not just get logits 
        # directly from a lookup table but go through an intermediate
        # embedding which is - n_embd dimensions in size
        
        # NOW WE 
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd) #nn.Embedding is a thin wrapper of a tensors of size (vocab_size,vocab_size) - will learn how to embed the tokens
        self.position_embedding_table = nn.Embedding(block_size,n_embd) #so each position from 0 to blocksize -1 in the context will get its own embedding - will learn how to embed posiitons
        self.key = nn.Linear(n_embd,head_size) #will learn how to convert nodes into keys
        self.query = nn.Linear(n_embd,head_size) #will learn how to convert nodes into queries
        self.value = nn.Linear(n_embd,head_size) #will learn how to represent that embeddings to get aggregated
        #i'm guessing this is overkill for this simple model but becomes important

        # then we want a linear layer to go from token embeddings to logits
        self.lm_head = nn.Linear(head_size, vocab_size) #will learn how to map from a node (which has been attention averaged) onto the output vocab

    def forward(self, idx, targets=None):  
        B, T = idx.shape #input batch number and block size

        tok_embd = self.token_embedding_table(idx) #  embed the tokens (B,T,C_emb)
        pos_embd = self.position_embedding_table(torch.arange(T,device = device)) #(T,C) # each position gets an embeddding
        x = tok_embd + pos_embd #x is the sum of the token embedding + position embedding (B,T,C)
        #note broadcasting is smart (B,T,C) + (T,C) second value gets right aligned to become (1,T,C) and then added to each input in hte batch

        # so now the model is "aware" of what position in the context the input is
        # ##BUT IT IS STILL ONLY USING ONE INPUT PER OUTPUT

        # as karpathy says "this is not helful for a bigram mdoel as it is
        # transation invariant" - the position doesnt help up really
        
        #bp()

        #adding in attention
        k = self.key(x) #(B,T,hs)
        q = self.query(x) #(B,T,hs)
        wei = q @ k.transpose(-2,-1) * head_size**-0.5 #(B,T,hs) @ (B,hs,T) -> (B,T,T)  #be careful what way around these go
        tril = torch.tril(torch.ones((T,T), device = device)) # (T,T)
        wei = wei.masked_fill(tril == 0, float("-inf")) #(B,T,T) - operation is broadcase across batch dimension
        wei = F.softmax(wei, dim = 1) #across 1st dimension = across each row

        #note you feed in a whole sequence but each node in that sequence predicts onto a target - hence hte explanation at the start of the video
        #karpathy is a legend

        v = self.value(x)
        attention_weighted_node = wei @ v #(B,T,T) @ (B,T,C) -> (B,T,C)
    
        logits = self.lm_head(attention_weighted_node) #FCLL to map reach node of C_embed dimensions onto the vocab dimensions (B,T,C_vocab)
        # remembder linear layers are also just matmuls + additino

        if targets is None:
            return logits
        else:        
            B,T,C = logits.shape
            logits = logits.view(B*T, C)
            targets = targets.clone().view(B*T)
            loss = F.cross_entropy(logits, targets)
        
        return logits, loss
    
    def generate(self, idx, max_new_tokens):
        with torch.no_grad():
            for _ in range(max_new_tokens):
                #bp()
                logits = self(idx[:,-8:]) 
                logits = logits[:, -1, :]
                probs = F.softmax(logits, dim = 1) 
                idx_next = torch.multinomial(probs, num_samples=1) 
                idx = torch.cat((idx,idx_next), dim = 1)
        return idx

model = BigramLanguageModel()
m = model.to(device)

#create optimizer
optimizer = torch.optim.Adam(model.parameters(), lr = learing_rate)

for iter in range(max_iters):

    #every once in a while evalue loss
    if iter % eval_interval ==0:
        losses = estimate_loss()
        print(f"step {iter}, {losses}")
        
        #print(f"step {iter}: train loss {losses['train']:.4f}, val loss {losses["val"]:.4f}")

    
    # extract data
    xb, yb = get_batch("train")
    # forward pass
    logits, loss = m(xb,yb)
    #zero gradient?
    optimizer.zero_grad(set_to_none = True)
    # backward pass - will populate the gradients
    loss.backward()
    # run optimizer - to step
    optimizer.step()

bp()
#use plt.imshow() to visualize the matrix

#generate from model
context = torch.zeros((1,1), dtype = torch.long, device=device)
print(decode(m.generate(context,max_new_tokens = 500)[0].tolist()))