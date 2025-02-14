#Creating a manual maximal marigin classifier
#Code stolen from 3D gauss

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import random

# set points
vectors = np.empty(shape = [4,0])
random.seed(20)
for i in range(1,10):
    v = np.array([[random.randint(1,10)],
     [random.randint(1,10)],
     [random.randint(1,10)]])
    #classify points based on simpe 
    # decision boundary (z - x = 0)
    c = [[1 if (v[2] - v[0] > 0) else -1]]
    
    vectors = np.append(
                vectors, 
                np.append(v,c,axis = 0), 
                axis = 1)
    
#Simple decision boundary #########################
#create a parametric plane
s = np.arange(0,10,0.1)
t = np.arange(0,10,0.1)
ss,tt = np.meshgrid(s,t)

#u,v are teh 2 vectors defing the plane
v = np.array([1,0,1])
u = np.array([0,1,0])

xb = 0 + v[0]*ss + u[0]*tt
yb = 0 + v[1]*ss + u[1]*tt
zb = 0 + v[2]*ss + u[2]*tt


#calculating marginal classifier












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


col = ["red" if i>0 else "blue" for i in vectors[3,:]]

ax.scatter(vectors[0,:],vectors[1,:],vectors[2,:],
          c = col)

ax.plot_surface(xb,yb,zb,
                alpha = 0.5,
                color = "grey")

plt.show()

