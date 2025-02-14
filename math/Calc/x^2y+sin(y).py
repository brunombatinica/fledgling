# 3D surface plot of the joint PDF of 2 standard normals

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
# colours
from matplotlib import cm

fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})

sd = 1
mu = 0

x = np.arange(-4*sd,4*sd,0.1)
y = np.arange(-4*sd,4*sd,0.1)
x,y = np.meshgrid(x,y)



#z = x*y - as we are assuming the 2 gausian distributions are independent
z = x**2 * y + np.sin(y)

#plot surface
surf = ax.plot_surface(x,y,z)

# set z set_axis_on
# Customize theaxis.
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)

plt.show()
