# binomial PMF
# binomial graph creator

#Illustrates that poisson approaches binomial for large n and small p

import sys
from functools import reduce
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#factorial calculator using gamma fucntion generator and then a np.array converter
def fact_gen(array):
    for i in array:
        try: 
            yield math.gamma(i+1)
        #catch math error from high factorials IT DOESN'T WORK
        except:
            yield sys.maxsize
            
            
def fact(array):
    return np.array(list(fact_gen(array)))

#safe factorial function
def safe_fact(x):
    try:
        return math.factorial(x)
    except:
        return 0


#initiallise inputs

n = 100
#n = int(input("How many trials? "))
#k = int(input("Number of successes? "))
p = 0.05
#p = float(input("Probability of success on a single trial (0.0 - 1.0)? "))


#Binomial -------------------------------------

#set up possible values
x = np.arange(0,n+1,1)
y1 = []

#P(k yes outcomes) = P^K * (1-P)*(n-k) * # of k yes sequences

y1 = ( np.power(p,x) * np.power((1 - p), (n - x)) ) * ( safe_fact(n) / (fact(x) * fact(n-x)) )


#Poisson approximation -----------------------------------------
l = n * p

#set up possible values
xrange = [0,n]
k = np.arange(*xrange,0.01)
#k = [*x] #this is the issue you turn it back inot a normal list which isnt good

y2 = ( np.power(l,k)  / fact(k) ) * np.exp(-1*l)

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
ax.set_xlim(0,n*p*3)
ax.set_ylim(0,max(y2)+0.02)
#moving axis to middle of plot (using spines)
#ax.spines['left'].set_position('zero')
#ax.spines['bottom'].set_position('zero')

#creat graphs
ax.bar(x,y1,0.4, align = "center")
ax.plot(k,y2)

#saves pdf and displays plot
#fig.savefig("binomial distribution.pdf")
plt.show()
