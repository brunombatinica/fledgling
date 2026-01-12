#%%
import torch; torch.manual_seed(0)
import torch.nn as nn
import torch.nn.functional as F
import torch.utils
import torch.distributions
import torchvision
import numpy as np
import matplotlib.pyplot as plt; plt.rcParams['figure.dpi'] = 200

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#%%
class Encoder(nn.Module):
    def __init__(self, input_size=784, hidden_size=512, latent_size=20):
        super(Encoder, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, latent_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

class Decoder(nn.Module):
    def __init__(self, latent_size=20, hidden_size=512, output_size=784):
        super(Decoder, self).__init__()
        self.fc1 = nn.Linear(latent_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, z):
        z = F.relu(self.fc1(z))
        z = self.fc2(z)
        return z.reshape(-1, 1, 28, 28) # reshape to (batch_size, 1, 28, 28) - image

class Autoencoder(nn.Module):
    def __init__(self, encoder, decoder):
        super(Autoencoder, self).__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, x):
        z = self.encoder(x)
        x_hat = self.decoder(z)
        return x_hat

#%%
encoder = Encoder(input_size=784, hidden_size=512, latent_size=20).to(device)
decoder = Decoder(latent_size=20, hidden_size=512, output_size=784).to(device)
autoencoder = Autoencoder(encoder, decoder).to(device)

#%%

