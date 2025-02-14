#Creating a manual maximal marigin classifier
#Code stolen from 3D gauss

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import random

# set points
vectors = np.empty(shape = [3,0])
random.seed(10)
for i in range(1,10):
    vectors = np.append(
                vectors, 
                [[random.randint(1,10)],
                 [random.randint(1,10)],
                 [random.randint(1,10)]], 
                axis = 1)
    
#Simple decision boundary #########################
#create a parametric plane
s = np.arange(-20,20,0.1)
t = np.arange(-20,20,0.1)
ss,tt = np.meshgrid(s,t)

#x0,y0,z0 are the "origin" leave it as 0,0,0 for now
x0 = 0
y0 = 0
z0 = 0

#u,v are teh 2 vectors defing the plane
v = np.array([1,0,1])
vi = v / np.sqrt(v.dot(v))

u = np.array([0,1,0])
yi = u / np.sqrt(u.dot(u))

x = x0 + v[0]*ss + u[0]*tt
y = y0 + v[1]*ss + u[1]*tt
z = z0 + v[2]*ss + u[2]*tt

##########################################
fig, ax = plt.subplots(subplot_kw = {"projection": "3d"})

# set z set_axis_on
# Customize theaxis.
ax.set_xlabel("x")
ax.set_xlim(0, 10)
ax.set_ylabel("y")
ax.set_ylim(0, 10)
ax.set_zlabel("z")
ax.set_zlim(0, 10)

ax.scatter(vectors[0,:],vectors[1,:],vectors[2,:])
ax.plot_surface(x,y,z)

plt.show()

