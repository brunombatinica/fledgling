#https://www.delftstack.com/howto/matplotlib/how-to-plot-a-circle-in-matplotlib/
# unfinished...

import numpy as np
import matplotlib as npl
import matplotlib.pyplot as plt

# setting up the range of x's and yx
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)

a,b = np.meshgrid(x,y)

c = a**2 + b**2

# sets up figure
fig, ax = plt.subplots()

ax.set_aspect(10)
ax.plot(x,y,color='C1')


#fig.savefig("figure.pdf")
plt.show()
