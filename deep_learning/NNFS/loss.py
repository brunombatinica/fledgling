import numpy as np
from matplotlib import pyplot as plt

class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output,y)
        #forward will depend on type of loss calculation
        data_loss = np.mean(sample_losses)
        return data_loss
    
class Loss_Crossentropy(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred) #could use y_true here
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)
        
        #calcualting ce depends on how y_true is passed in
        if len(y_true.shape) == 1:
            #scalar encoding of y_true
            ce = -np.log(y_pred_clipped[range(samples),y_true])
        elif len(y_true.shape) == 2:
            #onehot encoding
            ce = -np.dot(np.log(inputs),np.array(true_class))
            
        return ce #return negative log likelihoood

class Loss_Accuracy(Loss):
    def forward(self,y_pred,y_true):
        samples= len(y_pred)
        #*No need to clip here technically
        predictions = np.argmax(y_pred, axis = 1)
        
        if len(y_true.shape) == 1:
            #scalar encoding (from 0)
            b_table = [i == y_true[x] for i,x in enumerate(predictions)]
            
        if len(y_true.shape) == 2:
            #one hot encoding
            b_table = [y_true[i,predictions[i]] for i in range(samples)]
            
        return b_table
    
    
    
# x = np.arange(0.01,1,0.01)
# y = -x*np.log(x)

# plt.plot(x,y)


# softmax_output = 