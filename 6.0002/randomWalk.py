#random walk

import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import celluloid
from celluloid import Camera
import pandas as pd


class walker(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def step(self):
        #each step = north south east or west
        
        x = self.x
        y = self.y
        
        if random.randint(0,1):
            self.x = ( x + random.choice([-1,1] ) )
        else:
            self.y = ( y + random.choice([-1,1] ) )
    
    def getx(self):
        return self.x
    
    def gety(self):
        return self.y
    
    def getdistance(self):
        return (self.x**2 + self.y ** 2) ** 0.5
    

x = []
y = []
d = []

steps = 2000

drunk = walker(0,0)
random.seed(0)

for i in range(1,steps):
    x.append(drunk.getx())
    y.append(drunk.gety())
    d.append(drunk.getdistance())
    drunk.step()
    
fig = plt.figure() #creates figure
camera = Camera(fig) # creates camera

#Create plots seperately
ax = fig.add_subplot()

for i in range(steps):    
    ax.plot(x[0:i],y[0:i], color ='blue')
    ax.plot([i/100 for i in range(0,i)],d[0:i],color = "red")
    ax.set_xlim(-100,100)
    ax.set_ylim(-100,100)

    camera.snap() #takes a photos after each frame/iteration
    
animation = camera.animate(interval = 0.1, 
                           repeat = False, repeat_delay = 500)