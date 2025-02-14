#Lagrange multiplier and contour plot illustration

#example
# f = x**2 + y**2 (euclidean distance)
# g = xy = 3 constraint

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x1 = 5
y1 = 6

x2 = 4
y2 = 8

v1 = np.array([[x1,y1,0]])
v2 = np.array([[x2,y2,0]])

V = np.append(v1,v2,axis = 0)




fig,ax = plt.subplots()
ax.set_ylim(0,10)
ax.set_xlim(0,10)
ax.quiver(*np.zeros((2,2)),V[:,0],V[:,1],angles = "xy",scale_units = "xy",scale = 1.0)





