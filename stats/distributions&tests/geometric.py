# geometric PMF
# trials untill positive result


#import reduce function
from functools import reduce
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

n = 10 # to make it proper you could calculate a reasonable value given the probability
#k = int(input("Number of successes? "))
p = float(input("Probability of success on a single trial (0.0 - 1.0)? "))

#set up possible values
x = range(1,n+1)
y = []

for i in x:
    #P(k yes outcomes) = P^K * (1-P)*(n-k) * # of k yes sequences
    y.append( ((1-p) ** (i-1)) * p)

print(*y)
print(sum(y))

fig, ax = plt.subplots()

#puts grid on the plot
ax.grid()
#sets axes (default on)
ax.set_axis_on()
#set specific axis limits (made to roughly fit the data)
ax.set_xlim(-1,n+1)
ax.set_ylim(0,max(y)+0.02)
#moving axis to middle of plot (using spines)
#ax.spines['left'].set_position('zero')
#ax.spines['bottom'].set_position('zero')

#creat bar graph
ax.bar(x,y)

#saves pdf and displays plot
#fig.savefig("binomial distribution.pdf")
plt.show()
