import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fixing random state for reproducibility
np.random.seed(19680801)


def init():
    for line in lines:
        line.set_data_3d([],[],[])
    return lines

def plot_circle(x0,y0,r):
    #returns lines for circle at point x,y with radius r
    t = np.linspace(0,2*np.pi,100)
    x = x0 + r*np.sin(t)
    y = y0 + r*np.cos(t)
    
    return x,y

def update_lines(num,lines):    
    #Convert frame into parameter t, ranging from 0 - 4pi
    t = 4 * np.pi * (num / 200)
    
    
    #point 1 = position
    #point 1 = position
    x1 = [t-np.sin(t)]
    y1 = [-np.cos(t)]
    z1 = [0]
    
    #line 2 = circle
    x2, y2 = plot_circle(t,0,1)
    z2 = [0 for i in x2]
    
    #line 3 = velocity
    dx_dt = 1 - np.cos(t)
    dy_dt = np.sin(t)
    #line = vector
    x3 = np.array([0,dx_dt])
    y3 = np.array([0,dy_dt])
    #overlay onto position
    x3 = x3 + x1[0]
    y3 = y3 + y1[0]
    z3 = [0,0]
    
   
    xlist = [x1,x2,x3]
    ylist = [y1,y2,y3]
    zlist = [z1,z2,z3]
    
    #line 4 = acceleration
    
    for lnum, line in enumerate(lines):
        line.set_data_3d(xlist[lnum],ylist[lnum],zlist[lnum]) #set data for each line seperately
        
    return lines

# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

lines = []
line_colors = ["red","blue","orange","green","gray"]
line_format = ["o-","-","-","-","-"]
for i in range(3):
    line_object, = ax.plot([],[],[],line_format[i]) #ro places points at hte end of the line
    lines.append(line_object)

# Setting the axes properties
ax.set(xlim3d=(-10, 10), xlabel='X')
ax.set(ylim3d=(-10, 10), ylabel='Y')
ax.set(zlim3d=(-10, 10), zlabel='Z')

# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, frames = 100, fargs = (lines,),  interval=100)

plt.show()