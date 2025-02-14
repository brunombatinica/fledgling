

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

x = np.arange(0,1,.01)

gini = x * (1 - x)
D =  -1 *x * np.log(x)

fig = plt.figure()
ax = plt.axes()

ax.set_xlim([-1,2])
ax.set_ylim([-1,4])

ax = plt.plot(x,gini)
ax = plt.plot(x,D)

plt.show()



