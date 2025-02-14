# plotting a chi squared distribution

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

dof = 3
obs = 10000

x = np.zeros(obs)

for i in range(dof):
    x = np.c_[x, np.array(np.random.randn(obs) ** 2)]

x = np.sum(x, axis = 1)

f = x
#f = np.array(x1) + np.array(x2) + np.array(x3)

plt.hist(f, 100)
plt.show()
