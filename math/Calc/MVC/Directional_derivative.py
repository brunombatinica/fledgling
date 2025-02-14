import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
# colours
from matplotlib import cm

range_ = 2
x = np.arange(-range_,range_,0.1)
y = np.arange(-range_,range_,0.1)

X, Y = np.meshgrid(x,y)
#print(mx)

#function
Z = X**2 + Y**2

#partial derivatives
def nabla(point):
    x = point[0]
    y = point[1]
    dz_dx = 2*x
    dz_dy = 2*y
    return np.array([dz/dx, dz/dy])

#manual partial derivative vector directison
x = np.arange(-range_,range_,1)
y = np.arange(-range_,range_,1)
X_, Y_ = np.meshgrid(x,y)
scale = 5
grad_x = 2*X_ / scale
grad_y = 2*Y_ / scale




#point from which to find tangent plane
x_ = 0.5
y_ = 0.2
z_ = x_**2 + y_**2
p_ = np.array([x_,y_,z_])
dz_dx = 2*x_
dz_dy = 2*y_

zvx = np.array([1,0,dz_dx])
zvy = np.array([0,1,dz_dy])

#calculate plane using these 2 vectors
#normal vector
norm_ = np.cross(zvx,zvy)
print(norm_)

#intercept
C = np.dot(norm_,p_) 
#equation
Z_ = (C - norm_[0]*X - norm_[1]*Y)/norm_[2]





#different formulation
fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})

#gradient_field = ax.quiver(X,Y,0,grad_x,grad_y,0)
gradient_field = ax.quiver(x_,y_,0,dz_dx,dz_dy,0,color = "green")
norm = ax.quiver(p_[0],p_[1],p_[2],norm_[0],norm_[1],norm_[2],color = "red")
surf = ax.plot_surface(X,Y,Z,color = "blue", linewidth=0, alpha = 0.5)
pane = ax.plot_surface(X,Y,Z_, color = "gray",alpha = 0.5)


# set z set_axis_on
# Customize theaxis.
ax.set_xlim(-range_,range_)
ax.set_ylim(-range_, range_)
ax.set_zlim(0, 2*range_)

#ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
#ax.zaxis.set_major_formatter('{x:.02f}')
# Add a color bar which maps values to colors.

plt.show()

