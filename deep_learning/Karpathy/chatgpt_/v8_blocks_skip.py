#### Multihead attention

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
n_head = 4
n_embd = 32 # number of embedding demensions
max_iters = 5000
eval_interval = 300
learing_rate = 1e-3
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

class Head(nn.Module):
    def __init__(self, head_size):
        super().__init__()
        self.key = nn.Linear(n_embd,head_size, bias=False) #will learn how to convert nodes into keys
        self.query = nn.Linear(n_embd,head_size, bias=False) #will learn how to convert nodes into queries
        self.value = nn.Linear(n_embd,head_size, bias=False) #will learn how to represent that embeddings to get aggregated
        # tril is not a parameter so it is called a "buffer" in pytorch convention
        # registrer_buffer assigns this to the model as a buffer
        
        self.register_buffer("tril", torch.tril(torch.ones(block_size, block_size))) 
        
    def forward(self,x):
        B,T,C = x.shape
        
        #bp()
        q = self.query(x) #(B,T,C)
        k = self.key(x) #(B,T,C)

        #compute attention scores ("affinities")
        wei = q @ k.transpose(-1,-2) * C**-0.5 #(B,T,T)
        wei = wei.masked_fill(self.tril[:T,:T] == 0, float("-inf")) #make sure future does not communicate withe the past -> decoder block
        #bp()
        wei = F.softmax(wei, dim = -1) 

        v = self.value(x)
        out = wei @ v 
        return out    

class MultiHeadAttention(nn.Module):
    """multiple heads of self-attention in parrallel"""

    def __init__(self, n_head, head_size):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size) for _ in range(n_head)])
        # each head has a different random initialization

        #learns how to change the input to allow it to be 
        # added back into the residual pathway
        self.proj = nn.Linear(n_embd, n_embd) 
        
    def forward(self,x):
        out = torch.cat([h(x) for h in self.heads], dim = -1) 

        out = self.proj(out) #lienar transofrmation of hte output of the MHA
        # - projection back into the residual pathway ????
        return out

class FeedForward(nn.Module):
    """ a simple linear layer followed by a non-linearity"""

    #each token is passed in individually

    def __init__(self, n_embd):
        super().__init__()
        self.net = nn.Sequential(
            
            nn.Linear(n_embd, 4 * n_embd), #inner layer of ffwd is larger than input - just what the transformers paper did
            nn.ReLU(),
            nn.Linear(4 * n_embd, n_embd) #projection here - equivalent to self.proj in MHA
        )

    def forward(self,x):
        return self.net(x)

class Block(nn.Module):
    '''Transformer block: communcation followed by computation'''

    def __init__(self, n_embd, n_head):
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_head, head_size) #communcation
        self.ffwd = FeedForward(n_embd) #computation

    def forward(self, x):
        x = x + self.sa(x) #This is the residual connection
        x = x + self.ffwd(x)
        return x 

class AttentionLanguageModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd) #nn.Embedding is a thin wrapper of a tensors of size (vocab_size,vocab_size) - will learn how to embed the tokens
        self.position_embedding_table = nn.Embedding(block_size,n_embd) #so each position from 0 to blocksize -1 in the context will get its own embedding - will learn how to embed posiitons

        self.blocks = nn.Sequential(
            Block(n_embd, n_head = 4),
            Block(n_embd, n_head = 4),
            Block(n_embd, n_head = 4)
        )
        self.lm_head = nn.Linear(n_embd, vocab_size) #will learn how to map from a node (which has been attention averaged) onto the output vocab

    def forward(self, idx, targets=None):  
        B, T = idx.shape #input batch number and block size

        tok_embd = self.token_embedding_table(idx) #  embed the tokens (B,T,C_emb)
        pos_embd = self.position_embedding_table(torch.arange(T,device = device)) #(T,C) # each position gets an embeddding
        x = tok_embd + pos_embd #x is the sum of the token embedding + position embedding (B,T,C)
        x = self.blocks(x) #(B,T,C) #chains multiple MHA + ffwd
        logits = self.lm_head(x) 

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
                logits = self(idx[:,-block_size:]) #cant be longer then block size otherwise position embedding will not know what to do - only have block_size embeddings
                logits = logits[:, -1, :]
                probs = F.softmax(logits, dim = 1) 
                idx_next = torch.multinomial(probs, num_samples=1) 
                idx = torch.cat((idx,idx_next), dim = 1)
        return idx

model = AttentionLanguageModel()
m = model.to(device)

print(sum([i.nelement() for i in m.parameters()]))

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

#bp()
#use plt.imshow() to visualize the matrix

#generate from model
context = torch.zeros((1,1), dtype = torch.long, device=device)
print(decode(m.generate(context,max_new_tokens = 500)[0].tolist()))