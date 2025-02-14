# 3D parametric surface plot

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
# colours
from matplotlib import cm


fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})

#Parametric varaibles
# t = np.arange(0,2*np.pi,0.1)
# s = np.arange(0,2*np.pi,0.1)
# t,s = np.meshgrid(t,s)
angle = np.linspace(0,2*np.pi,100)
t,s = np.meshgrid(angle,angle)
    

#Parametric equations
x = 2*np.cos(t) + np.cos(t)*np.cos(s)
y = 2*np.sin(t) + np.sin(t)*np.cos(s)
z = np.sin(s)



#plot surface
surf = ax.plot_surface(x,y,z, linewidth=0, 
                       color ="w", antialiased=True )

# set z set_axis_on
# Customize theaxis.
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)

#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')
# Add a color bar which maps values to colors.

plt.show()
