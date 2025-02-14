import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

#importing our created functions
import os
os.chdir("C:/Users/bruno/OneDrive - The University of Auckland/Documents/code/python/ML/NNFS")
import Layers
import ActivationFunctions
import loss



#generating data
nnfs.init()
    #sets random seed and default datatype for dot product


X, y = spiral_data(samples = 100, classes = 3)
#plotting data
# plt.scatter(X[:,0].T,X[:,1].T, c = [int(i) for i in y])
# np.random.seed(0)
    

 
dense1 = Layer_Dense(2,3) # number of neurons is arbitrary
activation1 = Activation_ReLU()

dense2 = Layer_Dense(3,3)
activation2 = Activation_Softmax()
dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output) #softmax activation

#print(activation2.output[:5])

loss_function = Loss_Crossentropy()
loss = loss_function.calculate(activation2.output, y)

print(loss)
    




