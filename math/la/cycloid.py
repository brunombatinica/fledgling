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
ax.grid()
#sets axes (default on)
#ax.set_axis_off()
#set specific axis limits
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
########################################



t_ = np.arange(0,200,1)
#rotation argument
# divide i by number of frame to get 1 rotation


x_ = []
y_ = []
for i in t_:
    t = 2 * np.pi * (i / 100)
    #piston dimension
    r = 1
    v1x = -4 + r*t
    v1y = 0
    
    v2x = r * -np.sin(t)
    v2y = r * -np.cos(t)
    
    v3x = v1x + v2x
    v3y = v1y + v2y
    x_.append(v3x)
    y_.append(v3y)


def init():
    line.set_data([],[])
    return line,

def animate(i):
    
    
    #rotation argument
    # divide i by number of frame to get 1 rotation
    t = 2 * np.pi * (i / 100)
    
    #piston dimension
    r = 1
    v1x = -4 + r*t
    v1y = 0
    
    v2x = r * -np.sin(t)
    v2y = r * -np.cos(t)

    v3x = v1x + v2x
    v3y = v1y + v2y
    line.set_data([*x_[:i],v3x,v1x],[*y_[:i],v3y,v1y])
    
    return line,

anim = animation.FuncAnimation(fig, animate, init_func = init,
                               frames = 200, interval = 20, blit = True)

plt.show

