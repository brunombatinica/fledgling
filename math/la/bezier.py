# Quadratic bezier curve

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
ax.set_axis_on()
#set specific axis limits
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
########################################

curve1x = [0,2]
curve1y = [0,0]

curve2x = [2,3]
curve2y = [0,2]

curves = [curve1x,curve1y,curve2x,curve2y]
#Frames
f = 100


#Calculate te curve then display it
def bezier(f,curves):
    fx = []
    fy = []
    for i in range(f):
        qx, qy = q(i, curves)
        fx.append(qx[0] + i * (qx[1] - qx[0]) / f)
        fy.append(qy[0] + i * (qy[1] - qy[0]) / f)
        
    return fx, fy
    

def q(i, curves):

    q0x = curves[0][0] + i * (curves[0][1] - curves[0][0]) / f  
    q0y = curves[1][0] + i * (curves[1][1] - curves[1][0]) / f  

    q1x = curves[2][0] + i * (curves[2][1] - curves[2][0]) / f  
    q1y = curves[3][0] + i * (curves[3][1] + curves[3][0]) / f 
    
    qx = [q0x,q1x]
    qy = [q0y,q1y]
    return qx, qy


fx, fy = bezier(f,curves)
print(fx)
print(fy)
plt.plot(fx,fy)

def init():
    line.set_data([*fx],[*fy])
    return line,

def animate(i):
    origin=[0,0]
    
    qx, qy = q(i,curves)

    line.set_data([origin[0],*qx],[origin[1],*qy])
    
    return line,



anim = animation.FuncAnimation(fig, animate, init_func = init,
                               frames = f, interval = 20, blit = True)

plt.show

