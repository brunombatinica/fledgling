#approximating gauss using montecarlo
# as you do more random shifts the variability increases and hence the sd increases = wow

import numpy.random as rd
import matplotlib.pyplot as plt

def norm():
    a = 0
    for i in range(1000):
        #random number between -1 and 1
        a += rd.uniform(-1,1)
    return a

#degrees of freedom aka sources of variability (im not sure if this is the right term)
x = []

for i in range(1000):
    x.append(norm())

print(x)
num_bins = 20

n, bins, patches = plt.hist(x, num_bins,)
plt.show()
