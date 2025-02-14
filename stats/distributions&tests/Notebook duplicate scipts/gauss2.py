#using numpy to work out the 68% rule?????
# and computationally prove the variance formula
# I am really happy with this

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


mu = 0.5
sd = 2
x = np.linspace(-10,10,1000)
#print(x)

y = gaus(x,mu,sd)
#print(y)

#using trapezoidal rule
print("total probability = ",np.trapz(y,x))

##################################################################################################
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

###bootleg varaince calculator######################################################################
#var(X) = E[X^2]-E[X]^2

y2 = []
y3 = []

# calculate E[X] (y2) and E[X^2] (y3) - uses zip which is kinda cool
for i, j in zip(x,y):
    y2.append(j * i)
    y3.append(j * (i ** 2))

eX = np.trapz(y2,x)
print("E[X]= ",eX)

eX2 = np.trapz(y3,x)
print("E[x^2]= ",eX2)

# var(X)
vX = eX2 - (eX ** 2)
print("var(X)= ",vX)

# future challenge = actually writing this out myself
