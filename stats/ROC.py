#exploring the ROC curve with 
#bianry logistic regression

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

def logit(x,b0,b1):
    return np.exp(b0 + b1*x) / (1 + np.exp(b0 + b1*x))
    
def PR(x,prediction,indicator):
    # requires numpy
    pospred = prediction[indicator == 1]
    bool = pospred > x
    return (sum(bool)/len(bool))

def NR(x,prediction,indicator):
    # requires numpy
    pospred = prediction[ ~ (indicator == 1) ]
    bool = pospred < x
    return (sum(bool)/len(bool))  



#Fitting a logistic regression ot fake data
#### DONE IN R
#easier to work with numpy arrays
Y = np.array([0,0,0,0,0,1,1,1,1,1])
X = np.array([.1,.2,.25,.4,.6,.3,.5,.7,.8,.9])


# Hypothetical classifier s(x) 
# coefficients = -3.14, 0.69
coef = [-3.30,7.107]
x = np.arange(0,1,0.01)
s = logit(x,*coef)

#calculate prediction score for each data point
pred = logit(X,*coef)
print(pred)

#for each theta calculate the TPR and TNR
#Give it the same values as x for plotting convenience
#^ STUPID MAKES NO SENSE OT HAVE THEM ON HTE SAME AXIS
threshold = np.arange(0,1,0.01)



print(PR(0.29,pred,Y))

TPR = np.array([PR(i,pred,Y) for i in threshold])
TNR = np.array([NR(i,pred,Y) for i in threshold])


fig1,(ax1,ax2) = plt.subplots( 
        nrows = 1, ncols = 2)

#axis 1 - data exploration
ax1.scatter(X,Y)
ax1.scatter(X,pred, c = "red")
ax1.plot(x,s)
ax1.plot(TPR,threshold)
ax1.plot(TNR,threshold, c = "green")

#axis 2 - ROC curve
# plot of TPR against 1 - TNR
ax2.plot(1-TNR,TPR)

plt.show()

#PYPLOT STYLE
# fig = plt.figure()
# ax = plt.axes()

# ax.set_xlim([-1,2])
# ax.set_ylim([-1,4])

# #plotting 
# ax = plt.scatter(X,Y)
# ax = plt.scatter(X,pred, c = "red")
# ax = plt.plot(x,s)
# ax = plt.plot(TPR,threshold)
# ax = plt.plot(TNR,threshold, c = "green")



# plt.show()


##########################MISC CODE
# Smart list comprehension for general arrays but dont need to 
#be this clever when using numpy
# def PR(X,pred,Y):
#     #proportion of positive results 
#     #that are classified as positive
#     pospred = [j for i,j in enumerate(pred) if Y[i]]
#     print(pospred)
#     bool = [i>x for i in pospred]
#     return (sum(bool)/len(bool))

# def NR(X,pred,Y):
#     #proportion of negative results that are classified as negative
#     pospred = [j for i,j in enumerate(pred) if Y[i]]
#     bool = [i<x for i in pospred]
#     return (sum(bool)/len(bool))
