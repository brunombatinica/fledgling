import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# Recreating graph from 
# "Use and Misuse of the ROC Curve"

x = np.arange(-5,5,0.1)

def gauss(mean,sd,x):
    #returns probability of x given a 
    # normal distirbution with parameters 
    # mean and sd

    return 1/(sd * np.sqrt(2 * np.pi)) * \
        np.exp( -1/2 * ((x - mean)/sd)**2 )

def cdfgauss(mean,sd,x): 
    # cdf(x) for normal(mean,sd)
    
    X = np.arange(x,5*sd,0.01)
    
    Y = gauss(mean,sd,X)
      
    print("X",len(X))
    print("Y",len(Y))
    
    return 1 - np.trapz(Y, x = X) 
    
    


print((0.5 * np.log(3))/np.sqrt(2))

print(cdfgauss(0, 1, (0.5 * np.log(3))/np.sqrt(2)) )




# X1 = gauss(0,1,-4)

# #calculating mean of case group given the odds per 2 sd. 
# # beta = (muC - muNC) / sigma
# mu2 = 1

# fig, ax = plt.subplots()

# ax = plt.plot(x,X1)