# -*- coding: utf-8 -*-
# Animating a linear transformation
# WAIT FOR SET_XY position to be implemented



#importing important functions
import numpy as np
import matplotlib as npl
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib import animation



# set up figure and animation
fig, ax = plt.subplots()

#######################################
#choose style
plt.style.use('default')
#puts grid on the plot
ax.grid()
#sets axes (default on)
ax.set_axis_on()
#set specific axis limits
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
########################################

#initial coordinates
x = [0,1]
y = [0,0]

V = ax.quiver(x,y,0,0, 
         color = ("r", "r", "b", "g"),
         angles='xy',
         scale_units='xy',
         scale=1)

r = 1


#line y value moves 
def update(i):
    theta = 2 * np.pi * (i/100)
    x1 = np.cos(theta)
    y2 = np.sin(theta)
    
    V.set_UVC(x1,y2)
    return V,
    
#animation----
anim = animation.FuncAnimation(fig,
                               update,
                               frames = 100,
                               interval = 100,
                               blit = False)

#saves pdf and displays plot
#fig.savefig("vector.pdf")
plt.show()


