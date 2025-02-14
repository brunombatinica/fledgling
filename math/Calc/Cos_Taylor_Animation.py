import numpy as np
import matplotlib as mpl
from matplotlib import animation
from matplotlib import pyplot as plt

#Initialize stuff
frame_num = 100
x_limit = (-10,10)
y_limit = (-10,10)

# The maths
#Start with empty lists
x1,y1 = [],[]
x2,y2 = [],[]




#set up figure
fig = plt.figure()
ax1 = plt.axes(xlim = x_limit, ylim = y_limit)

#Create 2 lines???
lines = []
for i in range(2):
    line_object, = ax1.plot([],[])
    lines.append(line_object)

def init():
    for line in lines:
        line.set_data([],[])
    return lines

def animate(i):
    x = np.arange(-10,10,0.1)
    
    ### The actual math
    y1 = np.cos(x)
    y2 = np.cos(x+i)

    
    xlist = [x,x]
    ylist = [y1,y2]
    
    
    for lnum, line in enumerate(lines):
        line.set_data(xlist[lnum],ylist[lnum])
    
    return lines

# =============================================================================
# ###GENERAL FUNCTIONALITY TO BE ADDED IN....
#https://stackoverflow.com/questions/9876290/how-do-i-compute-derivative-using-numpy

# def taylor(func,i):
#     # input integer i and equation func
#     # returns the taylor equation of degree i
#     
# def fun(x):
#     # What function we want to examine
#     return np.cos(x)
# 
# def d_fun(x):
#     
# =============================================================================


# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frame_num, interval=10, blit=True)

