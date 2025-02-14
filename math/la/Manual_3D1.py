#Creating a bootleg 3D grapher based on this video:
#https://www.youtube.com/watch?v=SnK6ZbQggV4

# start with 2 circles

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# math

# set up polar coordinates
# continous for circles
#t = np.linspace(0, 2 * np.pi, 100)
# n sided shape
n = 4
#starting angle
theta = 0.4


t = np.linspace(theta,theta+2 * np.pi, n + 1)
r = 1



#circle 1
x1 = r * np.cos(t)
y1 = r * np.sin(t) + 2

#circle 2
x2 = r * np.cos(t)
y2 = r * np.sin(t) - 2


# verticle line



fig, ax = plt.subplots()

#######################################
#puts grid on the plot
ax.grid()
#sets axes (default on)
ax.set_axis_on()
#set specific axis limits
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
########################################

# plot circles
plt.plot(x1,y1)
plt.plot(x2,y2)


for i in range(0,4):
    plt.plot([x1[i],x2[i]],[y1[i],y2[i]])

#for i in range(n)

