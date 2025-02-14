# plotting a normal distribution in python and integrating over parts of it
# also mucking around with matplotlib

#importing important functions
import numpy as np
import matplotlib as npl
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt



def gaus(x,mu,sd):
    a = []
    for item in x:
        a.append( (1 / (sd * np.sqrt(2 * np.pi))) * np.exp( -0.5 * ((item - mu) / sd)**2) ) #mistakes for learning - using ^ instead of ** and using x instead of item
    return a

x = np.linspace(-5,5,100)
print(x)
mu = 0
sd = 1

y = gaus(x,mu,sd)

fig, ax = plt.subplots()



#puts grid on the plot
ax.grid()
#sets axes (default on)
ax.set_axis_on()
#set specific axis limits
ax.set_xlim(-5,5)
ax.set_ylim(0,1)
#moving axis to middle of plot (using spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

#acutal plot function
ax.plot(x,y,color = "C1")

#saves pdf and displays plot
fig.savefig("gaussian_distribution.pdf")
plt.show()
