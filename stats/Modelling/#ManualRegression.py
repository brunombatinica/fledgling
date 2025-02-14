#https://towardsdatascience.com/gradient-descent-animation-1-simple-linear-regression-e49315b24672
#very inefficient but quite clear

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
class mylr(object):
    def __init__(self,w = 1,b = 1, lr = 0.01):
        #where w = weight
        #b = bias
        #lr = learning rate
        
        self.lr = lr
        self.w = np.array([[w]])
        self.b = np.array([b])

    def cost(self,x,y):
        pred = x@self.w + self.b
        #@ performs matrix multiplication
        #for 1 predictor can simply times each element but wiht multiple weights 
        #need to use matrix multiplication to ensure the w1 is multplied by column 1 
        #simple LA stuff makes sense
        
        e = y - pred #error term
        
        return np.mean(e**2) # sum squares mean is equivalent to 1/n
    
    def fit(self,x,y): #THIS IS THE GRADIENT DESCENT ALGORITHM
        pred = x@self.w + self.b
        e = y - pred
        
        dj_dw = np.mean( (-2 * x) * e , axis = 0) #axis defined whether to return mean of rows or columns
        dj_db = np.mean( (-2) * e , axis = 0)
        
        self.w = self.w - self.lr*dj_dw #update w
        self.b = self.b - self.lr*dj_db #update b
    
    def predict(self,x):
        
        return (x@self.w + self.b)
    
    def params(self):
        #returns funciton parameters
        return (self.w,self.b)
    

xlim = (0,10)
ylim = (-20,10)
    
#create training data
random.seed(5)
# x_train = np.array([np.random.randint(*xlim, size = 10)]).T
# y_train = np.array([np.random.randint(*ylim, size = 10)]).T

x_train = np.array([[1,2,4,5,6,7]]).T
y_train = np.array([[4,-12,3,-11,-5,-17]]).T

# stick with numpy for now
# x = np.random.randint(10, size = 10)
# y = np.random.randint(10, size = 10)
# df = pd.DataFrame(data=numpy_data, columns=["x", "y"])

# Introduce lists where data is stored
w_list = [] #weights
b_list = [] #biases
c_list = [] #costs
ys_list = [] #stores the line value (y predictions for xs)
yhat_list = [] #yhat - predictions

xs = np.array([[-3,10]]).T # values of regression plot line



#########train model
model = mylr(w = 3, b = -1, lr = 0.001) # set random initial values and learning rate

for i in range(60000): #set number of epochs

    #extract w and b
    w_list.append(model.params()[0])
    b_list.append(model.params()[1])

    #calculate cost
    c_list.append(model.cost(x_train,y_train))
    
    #calculate y values of line
    ys_list.append(model.predict(xs).T)
    
    #calculate predicted y values of x to plot lines yhat -> y
    yhat_list.append(model.predict(x_train).T)
    
    #"train model" undergo 1 round of gradient descent
    model.fit(x_train,y_train)
    
#print parameters and costs after all epochs
print("weight: " + str(model.params()[0]))
print("y-intercept: " + str(model.params()[1]))    
print("RSS: " + str(model.cost(x_train,y_train))) #RSS



#compare it to the real thing....
reg = LinearRegression().fit(x_train,y_train)
print(reg.coef_)
print(reg.intercept_)

#animating the results
#Model changes very raplidly then slows down
#so use nonlinear time to plot epoch training to make it more smooth

#define which epochs to plot
a = np.arange(0,50,1).tolist()
b = np.arange(50,100,5).tolist()
c = np.arange(100,12000,200).tolist()
p = a + b + c

# turn lists into arrays then flatten them into 1d
w = np.array(w_list).flatten()
b = np.array(b_list).flatten()
c = np.array(c_list).flatten()    
ys = np.array(ys_list)
p = np.array(p)

#Create first animation
fig = plt.figure(figsize = (10,10)) #creates figure
labelsize_ = 14
camera = Camera(fig) # creates camera


#plot 1
def plot1():
    
    #Create plots seperately
    ax1 = fig.add_subplot(3,2,2)
    ax2 = fig.add_subplot(3,2,4, sharex = ax1) #right plots share x axis
    ax3 = fig.add_subplot(3,2,6, sharex = ax1)
    ax0 = fig.add_subplot(1,2,1)

    for i in p:
        #plot 1 - weights
        
        ax1.plot(w[0:i], color ='blue')
        ax1.set_title("w")
        ax1.tick_params(axis = "both", which = "major", labelsize = labelsize_)
           
        # #plot 2 - bias
        ax2.plot(b[0:i], color = "red")
        ax2.set_title("b")
        ax2.tick_params(axis = "both",which = "major", labelsize = labelsize_)
        
        # #plot 3 - cost  
        ax3.plot(c[0:i], color = "black")
        ax3.set_title("cost")
        ax3.tick_params(axis = "both", which = "major", labelsize = labelsize_)
        
        #plot 0 = the fit
        leg = ax0.plot(xs.T.flatten(),ys[i].flatten(), color = "r") #flatten arrays to get usable lists
        
        ax0.scatter(x_train,y_train,color = "blue")
        ax0.legend(leg,[f"epochs: {i}"], loc = "upper right")
        ax0.set_title("Linear Fit")
        ax0.set_xlabel("x")
        ax0.set_ylabel("y")
        ax0.set_ylim([-20,10])
        
        plt.tight_layout()
        camera.snap() #takes a photos after each frame/iteration
        
def plot2():
    #plots x and b with respect to cost
    
    ax0 = fig.add_subplot(2,1,1)
    ax1 = fig.add_subplot(2,2,3)
    ax2 = fig.add_subplot(2,2,4,sharex = ax1)
    
    for i in p:
        
        #plot 0 = the fit
        leg = ax0.plot(xs.T.flatten(),ys[i].flatten(), color = "r") #flatten arrays to get usable lists
        
        ax0.scatter(x_train,y_train,color = "blue")
        
        ax0.vlines(x_train.T, ymin = y_train.T, ymax = yhat_list[i] )
    
        ax0.legend(leg,[f"epochs: {i}"], loc = "upper right")
        ax0.set_title("Linear Fit")
        ax0.set_xlabel("x")
        ax0.set_ylabel("y")
        ax0.set_ylim([-20,10])
        
        
        #weight
        ax1.plot(w[0:i],c[0:i], color ='blue')
        ax1.set_title("w")
        ax1.tick_params(axis = "both", which = "major", labelsize = labelsize_)
           
        # #plot 2 - bias
        ax2.plot(b[0:i],c[0:i], color = "red")
        ax2.set_title("b")
        ax2.tick_params(axis = "both",which = "major", labelsize = labelsize_)
            
        camera.snap()
     
        
#visualising the cost function

def cost_3d(x,y,w,b):
    #predicts cost for every pair of w and b
    
    pred = x@w.T + b
    e = y - pred
    return np.mean(e**2)

ws = np.linspace(-5,5,10)
bs = np.linspace(-5,5,10)

W,B = np.meshgrid(ws,bs) # create meshgrid

zs = np.array(
    [
     cost_3d(x_train,y_train,np.array([[wp]]),np.array([[bp]])) for
                  wp,bp in zip(np.ravel(W), np.ravel(B))
    ]
)

Z = zs.reshape(W.shape) # get z values for survace plot in shape of W
        

def plot3():
    ax0 = fig.add_subplot(1,2,1)
    ax0.set_title("linaer fit")
    
    ax1 = fig.add_subplot(1,2,2, projection = '3d') # 3d projection
    ax1.set_title("Cost function")
    ax1.view_init(elev = 20, azim = 145)
                  
    for i in p:
        #plot 0 = the fit
        leg = ax0.plot(xs.T.flatten(),ys[i].flatten(), color = "r") #flatten arrays to get usable lists
        
        ax0.scatter(x_train,y_train,color = "blue")
        
        ax0.vlines(x_train.T, ymin = y_train.T, ymax = yhat_list[i] )
    
        ax0.legend(leg,[f"epochs: {i}"], loc = "upper right")
        ax0.set_xlabel("x")
        ax0.set_ylabel("y")
        ax0.set_ylim([-20,10])
        
        
        
        #cost function
        ax1.plot_surface(W,B,Z, rstride = 1, cstride = 1,color = "blue", alpha = 0.34)
        ax1.scatter(w[i],b[i],c[i], marker = "o",color = "red")
        
        ax1.set_xlabel("w")
        ax1.set_ylabel("b")        
        ax1.set_zlabel("cost")
     
        ax1.plot3D(w[0:i],b[0:i],c[0:i],  linestyle = "dashed",
                 linewidth = 2, color = "grey")
        
        camera.snap()
    
    
plot1()

#create animation
animation = camera.animate(interval = 10, 
                           repeat = False, repeat_delay = 500)

#save animation
#animation.save('linearreg.mp4', writer = "imagemagick")
    
    
        