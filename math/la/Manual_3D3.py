#Creating a bootleg 3D grapher based on this video:
#https://www.youtube.com/watch?v=SnK6ZbQggV4

# start with 2 circles

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import animation

# Set up the plot

fig, ax = plt.subplots()
line, = ax.plot([],[],lw = 2)

#######################################
#puts grid on the plot
#ax.grid()
#sets axes (default on)
ax.set_axis_off()
#set specific axis limits
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
########################################

#Inital function
def init():
    line.set_data([],[])
    return line,

#Actual animation
def animate(i):
    #rotation argument - set speec of rotation
    # divide i by number of frame to get 1 rotation
    tx = 0.5 * np.pi * (i / 100)
    ty = 2 * np.pi * (i / 100)
    
    #Do all the work here
    #vector = [x,y,z]
    #a = np.array( [[1,1,-1],[1,-1,-1],[-1,-1,-1],[-1,1,-1],[-1,1,1],[-1,-1,1],[1,-1,1],[1,1,1],[1,1,-1] ] )
    a = np.array( [[0,-1,0],[2,-1,0],[2,-1,2],[0,-1,2],[0,1,2],[2,1,2],[2,1,0],[0,1,0],[0,-1,0] ] )
    
    #viewing parameters
    # t = rotation around y axis

    b = []
    for i,vector in enumerate(a):
        b.append(cyl(pol(vector,tx),ty))

    c = np.array(b).T
    
    line.set_data(c[0],c[1])
    
    return line,

#Coverts array [x,y,z] to r,theta,z (cylindrical corrdinates)
def pol(a,t):
    x = a[0]
    y = a[1]
    z = a[2]
    
    # calculate r
    r = np.sqrt( np.power(x,2) + np.power(y,2) )
    
    #Calculate theta
    #Normal arctan only works for positive x
    theta1 = np.arctan2(x,y)
    
    # output = [r,theta,z]
    return np.array([r,theta1+t,z])

#Convert cylindrical coordinates a = [r,theta,z] and rotation term (t) to x,y
def cyl(a,t):
    persp = t
    r = a[0]
    theta = a[1]
    z = a[2]
    
    # print(r)
    # print(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)*np.sin(persp) + (z * np.cos(persp)) / np.cos(np.pi/4)    
    
    #print("OUTPUT:",np.array([x,y]))
    return np.array([x,y])



anim = animation.FuncAnimation(fig, animate, init_func = init,
                               frames = 200, interval = 20, blit = True)

plt.show

