#importing important functions
import numpy as np
import matplotlib as npl
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


x = np.linspace(-10,10,1000)
y = x

#plot figure
fig, ax = plt.subplots()

#puts grid on the plot
ax.grid()
#sets axes (default on)
ax.set_axis_on()
#set specific axis limits
ax.set_xlim(-sd*4,sd*4)
ax.set_ylim(0,max(y)+0.05)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

#acutal plot function
ax.plot(x,y,color = "C1")

#saves pdf and displays plot
#fig.savefig("gaussian_distribution.pdf")
plt.show()
