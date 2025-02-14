#PERSPECTIVE!!!

#Creating a bootleg 3D grapher based on this video:
#https://www.youtube.com/watch?v=SnK6ZbQggV4

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
    rx = 0.5 * np.pi * (i / 100)
    ry = 2 * np.pi * (i / 100)
    
    #vector = [x,y,z]
    a = np.array( [[1,1,-1],[1,-1,-1],[-1,-1,-1],[-1,1,-1],[-1,1,1],[-1,-1,1],[1,-1,1],[1,1,1],[1,1,-1] ] )
    #a = np.array( [[0,-1,0],[2,-1,0],[2,-1,2],[0,-1,2],[0,1,2],[2,1,2],[2,1,0],[0,1,0],[0,-1,0] ] )
    
    # coverts each [x,y,z] point (element in list a) into
    # list of [x,y] coordinates b
    b = []
    for i,vector in enumerate(a):
        #Convert [x,y,z] to cylindrical (polar) coordinates
        polar = xyz_to_cyl(vector)
        #converts cylindrial (polar) vector and rotation arguments to x,y
        xy = pol_to_xy(polar,rx,ry)
        #Appends each [x,y] to list b
        b.append(xy)
        
        
        
    # coverts b into an array
    # each row representing the [x,y] coordinates of a point
    # then transposes so each row is all the x and y coordinates 
    # respectively
    # this is how the line input is received
    c = np.array(b).T
    line.set_data(c[0],c[1])
    
    return line,

#Coverts vector [x,y,z] to r,theta,z (cylindrical corrdinates)
def xyz_to_cyl(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    
    # calculate r
    r = np.sqrt( np.power(x,2) + np.power(y,2) )
    
    #Calculate theta
    #Normal arctan only works for positive x
    theta = np.arctan2(x,y)
    
    # output = [r,theta,z]
    return np.array([r,theta,z])

#Convert cylindrical coordinates a = [r,theta,z] and rotation term (t) to x,y
def pol_to_xy(a,rx,ry):
    r = a[0]
    theta = a[1]
    z = a[2]
    
    # print(r)
    # print(theta)
    x = r * np.cos(theta + rx)
    y = r * np.sin(theta + rx)*np.sin(ry) + ((z * np.cos(ry))/np.cos(np.pi/4))    
    
    #print("OUTPUT:",np.array([x,y]))
    return np.array([x,y])

# Compute the z of a given point with given rotation
def z(a,rx,ry):
    1

anim = animation.FuncAnimation(fig, animate, init_func = init,
                               frames = 100, interval = 20, blit = True)

plt.show()

