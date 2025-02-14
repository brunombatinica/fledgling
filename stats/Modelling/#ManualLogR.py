#https://towardsdatascience.com/animations-of-logistic-regression-with-python-31f8c9cb420

import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import celluloid
from celluloid import Camera
import pandas as pd

from scipy.special import expit

import sklearn
from sklearn.linear_model import LogisticRegression

#simple logistiecregression model
class logreg(object):
    def __init__(self,lr = 0.01, p = 1):
        #initial guess = 0 for weights, 0.5 for bias
        
        
        self.lr = lr
        self.w = np.zeros((1,p))*0
        self.b = 0.5
        
        
    def crossentropy(self,x,y):
        #equivalent to log likelihood
        
        n = len(x)
        
        #initialize cross entropy
        j = 0
        for xi,yi in zip(x,y):
            zi = xi*self.w + self.b
            pi= 1 / (1 + np.exp( -1 * zi))
            
            j += yi * np.log(pi) + (1-yi)*np.log(1 - pi)
            
        J = -1/n * j
        
        return J
        
    
    
    def step(self,x,y): # actually perform the gradeint descent step
        #walks down the cross entropy function
        
        # print(self.w)
        
        n = len(x)
        
        dj_dw = 0
        dj_db = 0
        
        for xi,yi in zip(x,y):
            zi = xi*self.w + self.b
            pi= 1 / (1 + np.exp( -1 * zi))
            
            # print("parameters:")
            # print(xi)
            # print(yi)
            # print(zi)
            # print(pi)
            
            
            dj_dw += (pi - yi)*xi
            dj_db += (pi - yi)
            
        DJ_DW = 1/n * dj_dw
        DJ_DB = 1/n * dj_db
        
        # print("DJ_DW:",DJ_DW)
        
        self.w = self.w - self.lr*DJ_DW
        self.b = self.b - self.lr*DJ_DB
        
        
    
    def fit(self,x,y,n = 10): 
        #x,y, = data
        #n = number of epochs
        
        self.wlist = np.zeros((n,x.shape[1])) #x shape 1 gives number of predictors
        self.blist = np.zeros(n)
        self.celist = np.zeros(n)
        self.predlist = np.zeros((n,len(x))) #use to make conneciton lines - predictions of x
        #USED TO VISUALISE DIFFERENCE BETWEEN CE AND MSE - logr uses CE
        self.llist = np.zeros((n,4))
        
        for step in range(n):
            #for each step of gradient descent
            self.wlist[step] = self.w  
            self.blist[step] = self.b
            self.celist[step] = self.crossentropy(x,y)
            
            #self.llist[step] = self.predict() #line list
            
            self.predlist[step] = self.predict(x).T.flatten() #yvalues predicted by model flattened into a list
            self.step(x,y) #perform a step of gradient descent
    
    
    
    def predict(self,x):
        pred = np.zeros(len(x))
        for i,xi in enumerate(x):
            zi = xi*self.w + self.b
            pi= 1 / (1 + np.exp( -1 * zi))
            pred[i] = pi
            
        return pred
    
    def params(self):
        #returns funciton parameters
        return (self.w,self.b)
    
    
def predplane(w,x1,x2,b):
    y = x1*w[0] + x2*w[1] + b
    
    #array of size 4
    return y 


# Introduce training data:  
x_train = np.array([
    [-80],
    [-70],
    [-50],
    [-39],
    [-27],
    [-15],
    [-9],
    [12],
    [25],
    [36],
    [52],
    [65],
    [78],
    [90],
    [99],
    [110]
])

y_train = np.array([
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [1],
    [0],
    [1],
    [0],
    [1],
    [0],
    [1],
    [1],
    [1],
    [1]
])   



#########train model
model = logreg(lr = 0.001,p = 1) # set random initial values and learning rate
print("CE or inital:", model.crossentropy(x_train,y_train))
model.fit(x_train,y_train,100000)

print("MY ESTIAMTES:")
print(model.w.T)
print(model.b)

#compare to actaul MLR
reg = LogisticRegression().fit(x_train,y_train)
print("THE REAL DEAL")
print(reg.coef_)
print(reg.intercept_)



        
     
        






    
    
        