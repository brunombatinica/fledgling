#standard error
import numpy as np
import matplotlib as mpl
from matplotlib import animation
from matplotlib import pyplot as plt
from functools import reduce
from scipy.misc import derivative
import random

random.seed(100)
pop = [random.gauss(0,25) for i in range(100000)]

def getSamples(pop,n,amount):
    samples = []
    for i in range(amount):
        sample = random.sample(pop,n)
        samples.append(sample)
    return samples

def CSD(sample):
    mu = np.mean(sample)
    v = sum([(i - mu)**2 for i in sample])/(len(sample)-1)
    return v**0.5


samplesize = 3
s = getSamples(pop,samplesize,1000)

mhat = []
varhat = []
stdhat = []
bstd = []

for i in s:
    mhat.append(np.mean(i))
    varhat.append(np.var(i))
    stdhat.append(np.std(i))
    bstd.append(CSD(i))

#DISPLAY POPULATION SUMMARY
print("SUMMARY:")
print("POP MEAN:",np.mean(pop))
print("POP VAR:", np.var(pop))
print("POP STD:", np.var(pop)**0.5)
#print(np.var(pop)**0.5 * 1.96 * 2) #empirical rule overestimates as it is a uniform distribution

bins = 20

fig = plt.figure()
ax0 = plt.subplot(2,2,1)

ax0.hist(pop,50)
ax0.set_title("Population")

ax1 = plt.subplot(2,2,2)
ax1.hist(mhat,bins)
ax1.set_title("Sample means")
CI = [ np.mean(mhat) - 2*np.std(mhat),
      np.mean(mhat) + 2*np.std(mhat)]
print("SD of sample means:",np.std(mhat))
ax1.axvline(x = CI[0], c = "orange", lw = 0.5)
ax1.axvline(x = CI[1], c = "orange", lw = 0.5)


#runnign a 1 sample test
test = random.sample(pop,samplesize)
#print(test)
print("Sample mean: ", np.mean(test))
print("Estimated SE: ",end = '')
print(np.std(test) / len(test)**0.5)






# ax2 = plt.subplot(2,2,3)
# ax2.hist(varhat,bins,alpha = 0.5)
# ax2.axvline(x = np.var(pop), c = "r", lw = 0.5)
# ax2.set_title("Sample Variances")

ax3 = plt.subplot(2,2,3)
ax3.hist(stdhat,bins, alpha = 0.8)
ax3.axvline(x = np.std(pop), c = "r", lw = 0.5)
CI = [ np.mean(stdhat) - 2*np.std(stdhat),
      np.mean(stdhat) + 2*np.std(stdhat)]
ax3.axvline(x = CI[0], c = "orange", lw = 0.5)
ax3.axvline(x = CI[1], c = "orange", lw = 0.5)
ax3.set_title("Sample SD")


ax3 = plt.subplot(2,2,4)
ax3.hist(bstd,bins)
ax3.axvline(x = np.std(pop), c = "r", lw = 0.5)
ax3.set_title("Corrected SD")
