#https://www.delftstack.com/howto/matplotlib/how-to-plot-a-circle-in-matplotlib/

#importing important functions
import numpy as np
import matplotlib as npl
import matplotlib.pyplot as plt

# setting up the range of x's and yx
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)

a,b = np.meshgrid(x,y)

c = (a+0.5)**2 + (b)**2 - 1

# sets up figure
fig, ax = plt.subplots()

#creating graph
ax.contour(a,b,c,[0])
ax.set_aspect(1)

#fig.savefig("figure.pdf")
plt.axis([-10,10,-10,10])
plt.show()
