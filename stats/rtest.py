# plotting the function form appendix A in intro to R to see what the hell it looks like


import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
# colours
from matplotlib import cm


fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})

a = 1
b = 0

x = np.arange(-3,3,0.1)
y = np.arange(-3,3,0.1)

#start with a circle
x,y = np.meshgrid(x,y)

#z = 5 - 5 * (x **2 + y ** 2)
z = np.cos( y ) / (1 + x ** 2)

#plot surface
surf = ax.plot_surface(x,y,z, cmap=cm.coolwarm,linewidth=0, antialiased=False )

# set z set_axis_on
# Customize theaxis.
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-2, 2)

#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')
# Add a color bar which maps values to colors.

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
