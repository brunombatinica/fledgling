#Comparign geometric and exponential distributions

import sys
from functools import reduce
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt



#initiallise inputs

#n = 100
#n = int(input("How many trials? "))
#k = int(input("Number of successes? "))
p = 0.1
#p = float(input("Probability of success on a single trial (0.0 - 1.0)? "))


#Geometric -------------------------------------

#set up possible values
x1 = np.arange(0,n+1,1)
y1 = []

#P(k yes outcomes) = P^K * (1-P)*(n-k) * # of k yes sequences

y1 = np.power((1 - p), (x1)) * p


#exponential approximation -----------------------------------------
l = p #n * p

#set up possible values
xrange = [0,n]
x2 = np.arange(*xrange,0.01)
#k = [*x] #this is the issue you turn it back inot a normal list which isnt good

y2 = l * np.exp(-1*l*(x2))

#?more memory efficient way
#factk = np.fromiter(fact(k), float, count = -1)
#y = np.power(l,k) / factk




#Graphics ---------------------------------------------------

fig, ax = plt.subplots()

#puts grid on the plot
ax.grid()
#sets axes (default on)
ax.set_axis_on()
#set specific axis limits (made to roughly fit the data)
ax.set_xlim(0,10)
ax.set_ylim(0,max(y1)+0.02)
#moving axis to middle of plot (using spines)
#ax.spines['left'].set_position('zero')
#ax.spines['bottom'].set_position('zero')

#creat graphs
ax.bar(x1,y1,0.4, align = "center")
ax.plot(x2,y2)

#saves pdf and displays plot
#fig.savefig("binomial distribution.pdf")
plt.show()


