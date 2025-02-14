
#Basic animation using using funAnimation in mpl

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim = (0,1), ylim = (-2,2))

#Can unpack tuple here or create a tuple and work with it....
line, = ax.plot([], [], lw = 2)

#initializing function
def init():
    line.set_data([],[])
    return line,

def animate(i):
    x = np.linspace(0,2,1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x,y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func = init,
                    frames = 200, interval = 20, blit = True)

plt.show()
