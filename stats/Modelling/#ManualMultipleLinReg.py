#https://towardsdatascience.com/animations-of-multiple-linear-regression-with-python-73010a4d7b11


import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import celluloid
from celluloid import Camera
import pandas as pd

import sklearn
from sklearn.linear_model import LinearRegression

#simple linear regression model
class mlr(object):
    def __init__(self,lr = 0.01, p = 2):
        #initial guess = 1 for all :)
        
        self.lr = lr
        self.w = np.ones((1,p)).T
        self.b = np.ones((1,1)).T

    def cost(self,x,y):
        pred = x@self.w + self.b
        #@ performs matrix multiplication
        #for 1 predictor can simply times each element but wiht multiple weights 
        #need to use matrix multiplication to ensure the w1 is multplied by column 1 
        #simple LA stuff makes sense
        
        e = y - pred #error term
        
        return np.mean(e**2) # sum squares mean is equivalent to 1/n
    
    
    def step(self,x,y): # actually perform the gradeint descent step
        pred = x@self.w + self.b
        e = y - pred
        
        dj_dw = np.mean( (2 * e) * (-1 * x), axis = 0 ) #axis = 0 performs operation on each column!
        dj_db = np.mean( (2 * e) * -1 , axis = 0)
    
        self.w = (self.w.T - self.lr*dj_dw).T
        self.b = self.b - self.lr*dj_db
        
    
    def fit(self,x,y,n = 10000): 
        #x,y, = data
        #n = number of epochs
        
        self.wlist = np.zeros((n,x.shape[1])) #x shape 1 gives number of predictors
        self.blist = np.zeros(n)
        self.clist = np.zeros(n)
        self.predlist = np.zeros((n,len(x))) #use to make conneciton lines - predictions of x
        self.llist = np.zeros((n,4))
        
        for step in range(n):
            #for each step of gradient descent
            self.wlist[step] = self.w.T  #wlist has 2 columns each iteration is a new row - hence the single index which indexes rows
            self.blist[step] = self.b
            self.clist[step] = self.cost(x,y)
            
            #self.llist[step] = self.predict() #line list
            
            self.predlist[step] = self.predict(x).T.flatten() #yvalues predicted by model flattened into a list
            self.step(x,y) #perform a step of gradient descent
    
    def predict(self,x):
        
        return (x@self.w + self.b)
    
    def params(self):
        #returns funciton parameters
        return (self.w,self.b)
    
    
def predplane(w,x1,x2,b):
    y = x1*w[0] + x2*w[1] + b
    
    #array of size 4
    return y 


    
xlim = (0,10)
ylim = (-20,10)
    
#create training data
# random.seed(5)
# x_train = np.array([np.random.randint(*xlim, size = 10)]).T
# y_train = np.array([np.random.randint(*ylim, size = 10)]).T

x_train = np.array([ # two independent variables
    [1,-2],
    [2,1],
    [4,1],
    [5,-3],
    [6,4],
    [7,5]
])

y_train = np.array([ 
    [14],
    [-12],
    [-31],
    [-21],
    [-51],
    [-37]
])


#########train model
model = mlr(lr = 0.001,p = 2) # set random initial values and learning rate

model.fit(x_train,y_train,20000)

print("MY ESTIAMTES:")
print(model.w.T)
print(model.b)

#compare to actaul MLR
reg = LinearRegression().fit(x_train,y_train)
print("THE REAL DEAL")
print(reg.coef_)
print(reg.intercept_)


# Define which epochs to plot:
a1 = np.arange(0,50,1).tolist()
a2 = np.arange(50,100,5).tolist()
a3 = np.arange(100,1000,50).tolist()
a4 = np.arange(1000,20000,500).tolist()
p = a1+a2+a3+a4

#visualising this
#Create first animation
fig = plt.figure() #creates figure
camera = Camera(fig) # creates camera

x1lim = (-3,8)
x2lim = (-4,8)
x1 = np.linspace(*x1lim,2)
x2 = np.linspace(*x2lim,2)

X1,X2 = np.meshgrid(x1,x2)  #lowfidelity meshgrid




#plot 1
def plot1():
    
    ax0 = fig.add_subplot(projection = '3d') # 3d projection
    ax0.set_title("Visualization")
    #ax0.view_init(elev = 20, azim = 145)

    for i in p:
        
        #extract weights and bias
        w = model.wlist[i]
        b = model.blist[i]
        x = x_train 
        Z = np.array([predplane(w,x1,x2,b) for x1,x2 in zip(X1,X2)])
             
        #plot the hyperplane
        ax0.plot_surface( X1, X2, Z, rstride = 1, cstride = 1,color = "blue", alpha = 0.34)
        
        ax0.scatter(x_train[:,0], x_train[:,1], y_train, marker = "o",color = "red")
        
        ax0.set_xlabel("x1")
        ax0.set_ylabel("x2")        
        ax0.set_zlabel("y")
        
        camera.snap()
 
    
 
        
def predcost(w1,w2,b,x,y):
    yhat = x[:,0]*w1 + x[:,1]*w2 + b
    e = y - yhat.T
    #print(e)
    return np.mean(e**2)

def cost_3d(x,y,w,b):   # returns costs for every pair of w0 and w1.
        pred = x@w.T+b              
        e=y-pred
        return np.mean(e**2)
    
    

x_train = np.array([ # two independent variables
    [1,-2],
    [2,1],
    [4,1],
    [5,-3],
    [6,4],
    [7,5]
])

y_train = np.array([ 
    [14],
    [-12],
    [-31],
    [-21],
    [-51],
    [-37]
])

#plot 2
def plot2():
    
    ax0 = fig.add_subplot(1,2,1, projection = '3d') # 3d projection
    ax0.set_title("Visualization")
    #ax0.view_init(elev = 20, azim = 145)
    
    ax1 = fig.add_subplot(1,2,2)
    ax1.set_title("cost")
    #calculate cost function here
    #hold b constant so to visualise
    
    w1test = np.linspace(-15,5,50)
    w2test = np.linspace(-15,5,50)
    W1test,W2test = np.meshgrid(w1test,w2test)
    C = np.array(
        [predcost(w1,w2,np.array([[7.23]]),x_train,y_train) for 
         w1,w2 in zip(np.ravel(W1test),np.ravel(W2test))]
        )

    Cfin = C.reshape(W1test.shape)
    

    
    for i in p:
        
        #extract weights and bias
        w = model.wlist[i]
        b = model.blist[i]
        x = x_train 
        Z = np.array([predplane(w,x1,x2,b) for x1,x2 in zip(X1,X2)])
             
        #plot the hyperplane
        ax0.plot_surface( X1, X2, Z, rstride = 1, cstride = 1,color = "blue", alpha = 0.34)
        
        ax0.scatter(x_train[:,0], x_train[:,1], y_train, marker = "o",color = "red")
        
        ax0.set_xlabel("x1")
        ax0.set_ylabel("x2")        
        ax0.set_zlabel("y")
        
        
        #cost function
        ax1.contour(W1test,W2test,Cfin)
        
        
        
        
        camera.snap()
        
plot2()

animation = camera.animate(interval = 10, 
                           repeat = False, repeat_delay = 500)
    
        
     
        






    
    
        