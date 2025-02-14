# visualizing a multiple linear regression


import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
# colours
from matplotlib import cm

#Set up figure
fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})


x1 = np.arange(-4,4,0.1)
x2 = np.arange(-4,4,0.1)
#x1 = [0,1,2]
#x2 = [0,1,2] 

x1, x2 = np.meshgrid(x1,x2)
#print(mx)

#coefficients
b0 = 0
b1 = 1
b2 = 2

Y = np.exp(b0 + b1*x1 + b2*x2) / (1 + np.exp(b0 + b1*x1 + b2*x2))

#plot surface
surf = ax.plot_surface(x1,x2,Y, cmap=cm.coolwarm,linewidth=0, antialiased=False )

# set z set_axis_on
# Customize theaxis.
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(0, 1)

#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')
# Add a color bar which maps values to colors.

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


