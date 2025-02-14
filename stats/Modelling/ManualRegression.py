import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

v1 = [2,1]
v2 = [3,4]
v3 = [7,5]

data = np.array([v1,v2,v3])
print(data)

fig = plt.figure()
ax = plt.axes()
ax.set_xlim(0,10)
ax.set_ylim(0,10)

ax.scatter(data[:,0],data[:,1])

plt.show()