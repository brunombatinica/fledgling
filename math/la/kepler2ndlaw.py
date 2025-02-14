

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_lines(num,lines):    
    #Convert frame into parameter t, ranging from 0 - 4pi
    t = 4 * np.pi * (num / 200)
    
    #focus of ellipse = C
    a = 2
    b = 1.5
    c = np.sqrt(a**2 - b**2)
    #point 1 = com
    #com is focus of ellipse, com is com between sun and plane - will assume planet if of negligible size
    x1 = [0]
    y1 = [0]
    z1 = [0]
    
    #point 2 = planet
    x2 = [a*np.sin(t) - c]
    y2 = [b*np.cos(t)]
    z2 = [0]
    
    #point 3 = velocity
    
    #point 4 = acceleration
    x4 = 
    y4 = 
    z4 = [ ]
    
    
    
    
    # #line 3 = velocity
    # dx_dt = 1 - np.cos(t)
    # dy_dt = np.sin(t)
    # dz_dt = 1
    # #line = vector
    # x3 = np.array([0,dx_dt])
    # y3 = np.array([0,dy_dt])
    # z3 = np.array([0,dz_dt])
    # #overlay onto position
    # x3 = x3 + x1[0]
    # y3 = y3 + y1[0]
    # z3 = z3 + z1[0]
    
    # #line 4 = acceleration
    # d2x_dt2 = np.sin(t)
    # d2y_dt2 = np.cos(t)
    # d2z_dt2 = 0
    # #overlay onto position
    # x4 = np.array([0,d2x_dt2]) + x1
    # y4 = np.array([0,d2y_dt2]) + y1
    # z4 = np.array([0,d2z_dt2]) + z1
    
    #line 5 = trajectory
    global x_
    global y_
    global z_
    
    x_.append(x2[0])
    y_.append(y2[0])
    z_.append(z2[0])
    
    x5 = x_[:num]
    y5 = y_[:num]
    z5 = z_[:num]
   
    xlist = [x1,x2,x5]#,x3,x4,x5]
    ylist = [y1,y2,y5]#,y3,y4,y5]
    zlist = [z1,z2,z5]#,z3,z4,z5]
    
    #line 4 = acceleration
    
    for lnum, line in enumerate(lines):
        line.set_data_3d(xlist[lnum],ylist[lnum],zlist[lnum]) #set data for each line seperately
        
    return lines
    

# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

#set up global variables
x_ = []
y_ = []
z_ = []

lines = []
line_colors = ["red","blue","orange","green","gray"]
line_format = ["o-","o-","-","-","-"]
for i in range(3):
    line_object, = ax.plot([],[],[],line_format[i]) #ro places points at hte end of the line
    lines.append(line_object)

# Setting the axes properties
ax.set(xlim3d=(-4, 4), xlabel='X')
ax.set(ylim3d=(-4, 4), ylabel='Y')
ax.set(zlim3d=(-4, 4), zlabel='Z')

# Creating the Animation object
ani = animation.FuncAnimation(
    fig, update_lines, frames = 100, fargs = (lines,),  interval=20)

plt.show()