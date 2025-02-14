# stick breaking problem
#meshgrids indexed i,j*****


#using numpy to work out the 68% rule
# and computationally prove the variance formula
# I am really happy with this

#importing important functions
import numpy as np
import matplotlib as npl
import matplotlib.pyplot as plt

l = 1

x = np.linspace(0,l,11)
y = np.linspace(0,l,11)
X,Y = np.meshgrid(x,y, indexing ='ij')
print(X)
#print(Y)

#Z = X + Y
#print(Z)
#print("Z[1] =", Z[1,2])

'''
for index,num in np.ndenumerate(Z):
    print(index,num)
        if
'''
print("X[:,0]= ", X[:,0])
print("X[0,:]= ", X[0,:])


#just loop over each meshgrid and trim them
for i in range(0,len(X[0,:])):
    for j in range(0,len(X[:,0])):
        if j > i:
            X[i,j] = 0

#for i in range(0,len(Y[0,:])):
#    for j in range(0,len(Y[:,0])):
#        if j > i:
#            X[i,j] = 0

print(X)

"""
for i in Z:
    for j in i:
        #print (i,j)
        pass

#using trapezoidal rule
#print("total probability = ",np.trapz(y,x))


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
"""
