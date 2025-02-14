import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

class Activation_ReLU(object):
    def forward(self, inputs):
        self.output = np.maximum(0,inputs)

class Activation_Softmax(object):
    def forward(self, inputs):
        exp_values = (np.exp(inputs - np.max(inputs,axis = 1, keepdims = True)))
        prob = exp_values/np.sum(exp_values,axis = 1, keepdims = True)
        self.output = prob
        
        
        

# def ReLU(z):
#     # output = []
#     # for i in z:
#     #     output.append(max(0,i))
#     # return np.array(output)
    
#     #np versions
#     return np.maximum(0,z)




# #Exploring ReLU
# x = np.arange(-10,10,0.1)
# z1 = 1*x + 4
# l1 = ReLU(z1)
# z2 = -0.5 *l1 + 4
# l2 = ReLU(z2)
# z3 = -1.6*l2 + 10
# l3 = ReLU(z3)


# plt.grid()
# #plt.plot(x,z1, alpha = 0.5)
# plt.plot(x,l1, alpha = 0.5)
# #plt.plot(x,z2, alpha = 0.5)
# plt.plot(x,l2, alpha = 0.5)
# plt.plot(x,z3, alpha = 0.5)
# plt.plot(x,l3)
# plt.xlim(-10,10)
# plt.ylim(-10,10)
        



#Softmax activation