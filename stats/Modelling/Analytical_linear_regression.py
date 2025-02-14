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

#create training data
random.seed(5)
# x_train = np.array([np.random.randint(*xlim, size = 10)]).T
# y_train = np.array([np.random.randint(*ylim, size = 10)]).T

x = np.array([[1,2,4,5,6,7]]).T
y = np.array([[4,-12,3,-11,-5,-17]]).T

xmu = np.mean(x)
ymu = np.mean(y)

xc = x- xmu
yc = y - ymu

b = np.linalg.inv( xc.T@xc ) @ xc.T @yc


#compare it to the real thing....
reg = LinearRegression().fit(x_train,y_train)
print(reg.coef_)
print(reg.intercept_)









fig = plt.figure
ax0 = plt.subplot(1,2,1)

ax0.scatter(x,y)
ax0.scatter(xmu,ymu,c = "red")

ax1 = plt.subplot(1,2,2)

ax1.scatter(xc,yc)
ax1.scatter(np.mean(xc),np.mean(yc), c = "red")
    
print(b)   