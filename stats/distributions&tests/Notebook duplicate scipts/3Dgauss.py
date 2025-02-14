# 3D surface plot of the joint PDF of 2 standard normals

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
# colours
from matplotlib import cm

#gausian distribution calculator
def gaus(x,mu,sd):
    a = []
    for item in x:
        a.append( (1 / (sd * np.sqrt(2 * np.pi))) * np.exp( -0.5 * ((item - mu) / sd)**2) ) #mistakes for learning - using ^ instead of ** and using x instead of item
    return a


fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})

sd = 1
mu = 0

x = np.arange(-4*sd,4*sd,0.1)
y = np.arange(-4*sd,4*sd,0.1)
x,y = np.meshgrid(x,y)



#z = x*y - as we are assuming the 2 gausian distributions are independent
z = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp( -0.5 * ( ((x - mu) / sd)**2 + ((y - mu) / sd)**2))

#plot surface
surf = ax.plot_surface(x,y,z, cmap=cm.coolwarm,linewidth=0, antialiased=False )

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
