import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

xlim = [-10,10]
ylim = [-10,10]
x = np.arange(*xlim,0.01)

y1 = np.log(x)
y2 = np.exp(x)

fig, ax = plt.subplots()

ax.set_xlim (*xlim)
ax.set_ylim (*ylim)

ax = plt.plot(x,y1)
ax = plt.plot(x,y2)

