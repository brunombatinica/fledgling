# Basic train animation

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
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
########################################


def init():
    line.set_data([],[])
    return line,

def animate(i):
    #piston dimension
    r1 = 1
    r2 = 2 # must be greater than r1
    
    #rotation argument
    # divide i by number of frame to get 1 rotation
    t1 = 2 * np.pi * (i / 100)
    t2 = np.arccos(r1 / r2 * np.cos(t1))
    
    origin = [0,0]
    
    
    x1 = r1 * np.cos(t1)
    y1 = r1 * np.sin(t1)
    
    
    x2 = 0
    y2 = y1 + r2 * np.sin(t2)
    

    
    line.set_data([origin[0],x1,x2],[origin[1],y1,y2])
    
    return line,

anim = animation.FuncAnimation(fig, animate, init_func = init,
                               frames = 100, interval = 20, blit = True)

plt.show

