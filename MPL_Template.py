#importing important functions
import numpy as np
import matplotlib as npl
import matplotlib.pyplot as plt



fig, ax = plt.subplots()

#######################################
#puts grid on the plot
ax.grid()
#sets axes (default on)
ax.set_axis_on()
#set specific axis limits
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
########################################

#acutal plot function


#saves pdf and displays plot
#fig.savefig("vector.pdf")
plt.show()
