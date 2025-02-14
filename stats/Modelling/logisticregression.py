# visualizing a single binary linear regression


import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
# colours
from matplotlib import cm




x1 = np.arange(-10,10,0.1)


#coefficients
b0 = -5
b1 = 0.8


Y = np.exp(b0 + b1*x1) / (1 + np.exp(b0 + b1*x1))


fig, ax = plt.subplots()

#z = x*y - as we are assuming the 2 gausian distributions are independent
#z = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp( -0.5 * ( ((x - mu) / sd)**2 + ((y - mu) / sd)**2))
#simplified gaus
#Y = np.exp(-1*np.abs(x.T@cov_1@x))


#plot surface
surf = ax.plot(x1,Y)

# set z set_axis_on
# Customize theaxis.
ax.set_xlim(-10, 10)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')
# Add a color bar which maps values to colors.

plt.show()


