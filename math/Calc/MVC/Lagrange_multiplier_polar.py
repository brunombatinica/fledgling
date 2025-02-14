#Lagrange multiplier and contour plot illustration

#example
# f = x**2 + y**2 (euclidean distance)
# g = xy = 3 constraint

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
X,Y = np.meshgrid(x,y)

f = X**2 + Y**2

t = np.linspace(0,np.pi,1000)
r = np.sqrt(6/np.sin(2*t))
gy = r*np.cos(t)
gx = r*np.sin(t)

#direvtional derivative of f
fx = 2*x
fy = 2*y


fig,ax = plt.subplots()
ax.set_ylim(0,10)
ax.set_xlim(0,10)
ax.contour(X,Y,f, [i for i in range(0,100,10)])
ax.plot(gx,gy,color = "red")

ax.quiver(0,0,1,1)

