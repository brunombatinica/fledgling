# Basic train animation

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import animation


# Set up the plot

fig, ax = plt.subplots()

#######################################
#puts grid on the plot
ax.grid()
#sets axes (default on)
#ax.set_axis_off()
#set specific axis limits
ax.set_xlim(-2,10)
ax.set_ylim(-5,5)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
########################################


lines = []
line_colors = ["red","blue","orange","green","gray"]
line_format = ["o-","-","-","-","-"]
for i in range(5):
    line_object, = ax.plot([],[],line_format[i],lw = 2, color = line_colors[i] ) #ro places points at hte end of the line
    lines.append(line_object)

def plot_circle(x0,y0,r):
    #returns lines for circle at point x,y with radius r
    t = np.linspace(0,2*np.pi,100)
    x = x0 + r*np.sin(t)
    y = y0 + r*np.cos(t)
    
    return x,y
    
def init():
    for line in lines:
        line.set_data([],[])
    return lines

#set global varaibles for trajectory
x_ = []
y_ = []

def animate(i):
    #Convert frame into parameter t, ranging from 0 - 4pi
    t = 4 * np.pi * (i / 200)
    
    #point 1 = position
    x1 = [t-np.sin(t)]
    y1 = [-np.cos(t)]
    
    #line 2 = circle
    x2, y2 = plot_circle(t,0,1)
    
    #line 3 = velocity
    dx_dt = 1 - np.cos(t)
    dy_dt = np.sin(t)
    #line = vector
    x3 = np.array([0,dx_dt])
    y3 = np.array([0,dy_dt])
    #overlay onto position
    x3 = x3 + x1[0]
    y3 = y3 + y1[0]
    
    #line 4 = acceleration
    d2x_dt2 = np.sin(t)
    d2y_dt2 = np.cos(t)
    #overlay onto position
    x4 = np.array([0,d2x_dt2]) + x1
    y4 = np.array([0,d2y_dt2]) + y1
    
    
    #line 5 = trajectory
    global x_
    global y_
    
    x_.append(x1)
    y_.append(y1)
    
    x5 = x_[:i]
    y5 = y_[:i]
    
   
    xlist = [x1,x2,x3,x4,x5]
    ylist = [y1,y2,y3,y4,y5]
    
    #line 4 = acceleration
    
    for lnum, line in enumerate(lines):
        line.set_data(xlist[lnum],ylist[lnum]) #set data for each line seperately
        
    return lines

anim = animation.FuncAnimation(fig, animate, init_func = init,
                               frames = 200, interval = 20, blit = True)

plt.show()

