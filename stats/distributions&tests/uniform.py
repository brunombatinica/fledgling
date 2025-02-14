#uniform distribution using montecarlo

import numpy.random as rd
import matplotlib.pyplot as plt

#degrees of freedom aka sources of variability (im not sure if this is the right term)
df = 100

x = []
#random number between -1 and 1

for i in range(10000):
    x.append(rd.uniform(-1,1))

num_bins = 20

n, bins, patches = plt.hist(x, num_bins, range=(-1,1))
plt.show()
