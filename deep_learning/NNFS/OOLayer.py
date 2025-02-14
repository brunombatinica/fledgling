import numpy as np
import nnfs
from matplotlib import pyplot as plt
from nnfs.datasets import spiral_data

class Layer_Dense(object):
    def __init__(self, n_inputs, n_neurons):
    
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons) #randn = gauss at 0
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
        
# def create_data(points, classes):
#     X = np.zeros((points*classes,2))
#     y = np.zeros(points*classes, dtype = "uint8")
#     for class_number in range(classes):
#         ix = range(points*class_number, points*(class_number + 1))
#         r = np.linspace(0.0,1, points) # radius
#         t = np.linspace(class_number*4, (class_number + 1)*4, points) + np.random.randn(points)*0.2 #theta between class_number and class_number+1 plus some random error
#         X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
#         y[ix] = class_number 
#     return X, y    

class Activation_Softmax(object):
    def forward(self, inputs):
        exp_values = (np.exp(inputs - np.max(inputs,axis = 1, keepdims = True)))
        prob = exp_values/np.sum(exp_values,axis = 1, keepdims = True)
        self.output = prob
        
# class Activation_Crossentropy(object):
#     def forward(self, inputs, true_class):
#         #true class is onehot encoding
#         self.output = -1*np.dot(np.log(inputs),np.array(true_class))
        
# class Activation_Crossentropy(object): 
#     def forward(self, softmax_outputs, class_targets):
#         output = []
#         for targ_idx, distribution in zip(class_targets, softmax_outputs):
#             output.append( -1*np.log(distribution[targ_idx]))
#         #true class is a class number
#         self.output = output
        
# class Activation_Crossentropy(object):
#     #need to consider 0
#     def forward(self, softmax_outputs, class_targets):
#         y_pred = softmax_outputs
#         y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7) #prevents results of 0
#         ce = -np.log(y_pred_clipped[range(len(y_pred_clipped)),class_targets])
#         self.output = np.mean(ce)       
        
        
class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output,y) #returns list of costs of each output
        
        #forward will depend on type of loss calculation
        data_loss = np.mean(sample_losses)
        return data_loss
    
class Loss_Crossentropy(Loss):
    def forward(self, y_hat, y):
        #y_pred = matrix of prediction
        #y_true = either matrix of 1 hot encoded or vector of scalar class results
        

        y_hat_clipped = np.clip(y_hat, 1e-7, 1-1e-7)
        
        #calcualting ce depends on how y_true is passed in
        if len(y.shape) == 1:
            #scalar encoding of y_true
            
            #np.log naturaly does row wise operations...
            ce = -np.log(y_hat_clipped[range(len(y)),y]) #indexing using range important
            
        elif len(y.shape) == 2:
            #onehot encoding
            ce = sum(np.log(y_hat*y),axis = 1)
            
        return ce #returns list of log likelihoods for each sample input

class Loss_Accuracy(Loss):
    def forward(self,y_hat,y):
        samples= len(y_hat)
        
        #*No need to clip here technically
        predictions = np.argmax(y_hat, axis = 1)
        
        if len(y.shape) == 1:
            #scalar encoding (from 0)
            b_table = [i == y[x] for i,x in enumerate(predictions)]
            
        if len(y.shape) == 2:
            #one hot encoding
            b_table = [y[i,predictions[i]] for i in range(samples)]
            
        return b_table
    
#testing accuracy
# test_pred = np.array([[0.1,0.1,0.5],[0.2,0.6,0.1],[0.1,0.01,0.01]])
# y_true_s = np.array([2,2,0])
# y_true_oh = np.array([[0,1,0],[0,1,0],[1,0,0]])
# a = Loss_Accuracy()
# print(a.calculate(test_pred,y_true_s))
# print(a.calculate(test_pred,y_true_oh))

#np.random.seed(0)
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
loss = loss_function.calculate(activation2.output[[0]], y[[0]])

print(loss)
    
    






