##### SIMPLE BIGRAM - BUT CODED AS A NN

import torch
import torch.nn as nn
from torch.nn import functional as F

# hyperparameters
batch_size = 32 #number of independent sequences
block_size = 8  #maximum context length of our prediciton \
# (in reality only the last element is used for the bigram model)
max_iters = 3000
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
    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size) #nn.Embedding is a thin wrapper of a tensors of size (vocab_size,vocab_size) essentially a lookup table

    def forward(self, idx, targets=None):  
        logits = self.token_embedding_table(idx) 

        if targets is None:
            return self.token_embedding_table(idx)
        else:        
            B,T,C = logits.shape
            logits = logits.view(B*T, C)
            targets = targets.clone().view(B*T)
            loss = F.cross_entropy(logits, targets)
        
        return logits, loss
    
    def generate(self, idx, max_new_tokens):
        for _ in range(max_new_tokens):
            logits = self(idx) 
            logits = logits[:, -1, :]
            probs = F.softmax(logits, dim = 1) 
            idx_next = torch.multinomial(probs, num_samples=1) 
            idx = torch.cat((idx,idx_next), dim = 1)

        return idx

model = BigramLanguageModel(vocab_size)
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

#generate from model
context = torch.zeros((1,1), dtype = torch.long, device=device)
print(decode(m.generate(context,max_new_tokens = 500)[0].tolist()))