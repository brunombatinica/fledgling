import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

def v2p(v):
    x = [0,v[0]]
    y = [0,v[1]]
    return x, y

x = [1,0]
y = [0,1]

v1 = np.array([1,1])

i = [1,0]
j = [1,1]

T = np.array([i,j]).T

v2 = T @ v1

print(T)
print(v2)

fig, ax = plt.subplots()

ax.plot(*v2p(x))
ax.plot(*v2p(y))
ax.plot(*v2p(v1))
ax.plot(*v2p(i))
ax.plot(*v2p(j))
ax.plot(*v2p(v2))

#######################################
#puts grid on the plot
ax.grid()
#sets axes (default on)
ax.set_axis_on()
#set specific axis limits
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
########################################