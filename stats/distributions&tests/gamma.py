# 3d plot of the gamm function

import numpy as np
from scipy.special import gamma as gamma
import matplotlib.pyplot as plt
# colours
from matplotlib import cm

x = np.arange(-5,5,.01)
y = np.arange(-5,5,.01)
y_complex = 1j * y

print(y)


X,Y = np.meshgrid(x,y_complex)
x,y = np.meshgrid(x,y)

print(X + Y)

z = np.abs(gamma(X + Y))

print(z)

fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})

#set specific axis limits
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(0, 10)

#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')
# Add a color bar which maps values to colors.

#acutal plot function
surf = ax.plot_surface(x,y,z )

#fig.colorbar(surf, shrink=0.5, aspect=5)

#saves pdf and displays plot
#fig.savefig("gamma function.pdf")
plt.show()
