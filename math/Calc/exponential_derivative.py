import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

x = np.arange(0,100,1)
dt = 0.000000001
c = (x ** (dt) - 1) / (dt)
print(c)

fig, ax = plt.subplots()

ax.set_xlim (0,100)
ax.set_ylim (0,10)

ax = plt.plot(x,c)

