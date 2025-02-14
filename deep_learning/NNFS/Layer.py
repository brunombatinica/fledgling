import numpy as np

inputs = np.array([1,2,3,2.5],
                  )

weights = np.array([[0.2,0.8,-0.5,1],
            [0.5,-0.91,0.26,-0.5],
            [-0.26,-0.27,0.17,0.87]])

biases = np.array([2, 3, 0.5])

output = np.dot(weights,inputs) + biases
print(output)




##OO LAYERS
import numpy as np
import nnsf

nnfs.init()
    #sets random seed and default datatype for dot product




np.random.seed(0)

X = np.array([[1.0, 2.0 ,3.0 ,2.5],
              [2.0, 5.0,-1.0, 2.0],
              [-1.5,2.7, 3.3,-0.8]])

inputs - [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
for

n_inputs = X.shape[1] # number of columns = lengths of each input, number of features in each sampe

class Layer_Dense(object):
    def __init__(self, n_inputs, n_neurons):
    
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons) #randn = gauss at 0
        self.biases = np.zeros((1, n_neurons))
        
        #could automate this by simply passing in inputs and neural network initializing itself....
        
        

    def forward(self, inputs):
        #takes inputs and returns the outputs of the layer in the same form
        
        # #could check shape of inputs
        # if inputs.shape[1] not self.weights.shape[0]:
        #     return("incorrect dimensions of input")
        
        self.output = np.dot(inputs,self.weights) + self.biases 

        
        
class Activation_ReLU(object):
    def forward(self, inputs):
        self.output = np.maximum(0,inputs)
    
    
layer1 = Layer_Dense(4,5) # number of neurons is arbitrary
layer2 = Layer_Dense(layer1.weights.shape[1] , 2) #number inputs determined by size of previous layer 
    
    
layer1.forward(X)
layer2.forward(layer1.output)
#print(layer1.output)
print(layer2.output)