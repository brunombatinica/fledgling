
#Lagrange multiplier and contour plot illustration

#example
# f = x**2 + y**2 (euclidean distance)
# g = xy = 3 constraint

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x_mesh = np.linspace(-10,10,100)
y_mesh = np.linspace(-10,10,100)
X,Y = np.meshgrid(x_mesh,y_mesh)






#input
x = np.sqrt(3)


#work out position of constraing
y = 3/x

#direvtional derivative of f
f = X**2 + Y**2
fx = 2*x
fy = 2*y

#directional derivative of g
gy_ = 3/x_mesh
gx = y
gy = x

#finding solution with lagrange.....
np.array([])


fig,ax = plt.subplots()
ax.set_ylim(0,10)
ax.set_xlim(0,10)
ax.contour(X,Y,f, [i for i in range(0,100,10)], colors = "blue")
ax.plot(x_mesh,gy_,color = "red")

ax.quiver(x,y,fx/100,fy/100,color = "blue", scale = True)
ax.quiver(x,y,gx/100,gy/100,color = "red", scale = True)



