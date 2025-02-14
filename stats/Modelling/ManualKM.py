#simple code for running a manual KM test

import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from sksurv.nonparametric import kaplan_meier_estimator

from sksurv.datasets import load_veterans_lung_cancer

data_x, data_y = load_veterans_lung_cancer()

#print(data_x)
#print(data_y[[1]])
#read data-----------
dat = pd.DataFrame.from_records(data_y)
                           
print(dat)

raw_time = dat["Survival_in_days"]
bool_ind = dat["Status"]

#randomly generated tree --------
# np.random.seed(20)
# ind = np.random.randint(2, size = 10)
# bool_ind = list(map(bool,ind))
# raw_time = np.array(sorted(np.random.randint(100, size = 10)))

#manual inputs------------------
#bool_ind = list(map(bool, [0,1,0,0,1,0,0] ))
#raw_time = np.array([4,5,6,6,7,8,9])

#dat = pd.DataFrame(np.array([bool_ind,raw_time]).T,
#                  columns = ["Status","Survival_in_days"])
# convert = {"Status": bool,
#            "Survival_in_days":int}
# dat = dat.astype(convert)


time, survival_prob = \
    kaplan_meier_estimator(dat["Status"], dat["Survival_in_days"])
    

def KM(t,i):
    #manually computes the KM curve from times t and indicator variable i
    #both as np.arrays
    
    #Poorly written but works perfectly
    #Handles ties
    
    print(t)
    print(i)
    
    #Need to first sort arrays in terms of time
    t,i = (np.array(k) for k in zip(*sorted(zip(t,i))))
    
    print(t)
    print(i)
    
    #array of UNIQUE (set(ti)) event times d1...dk
    #add time = 0 aswell
    d = np.append(np.array([0]),list(set(t[i])))
    d = sorted(d)
    
    print(d)
    
    #array for of survival estimate s(d1)....s(dk)
    #s(0) = 1
    s = [1]
    
    
    for ind,x in enumerate(d[1:]):
        #risk set calculation = 
        #print(x)
        
        #people alive just before dk = risk set
        r = len(t[t >= x])
        
        #how many die at that time t[i]
        q = 0
        for j in range(len(t)):
            if t[j] == x and i[j] == True:
                q += 1

        #survival probability
        s.append( s[-1] * ((r - q)/r) )
       
    plt.step(d,s,where = "post")
    
    return d,s

fig, ax = plt.subplots()




ax.set_ylim(0,1)
ax.set_xlim(0,1000)
# plotting
#plt.step(time,survival_prob, where = "post")
#plt.step([0,0.5,4],[1,0.5,0.5],where = "post")

plt.step(time,survival_prob, where = "post")
#d,s = KM(list(raw_time),list(bool_ind))

print(time)
print(survival_prob)
print(d[1:])
print(s)



# #testing
# print(time)
# print(len(time))
# #print(raw_time)
# print(list(raw_time))
# print("Raw TIme:", len(raw_time))
# print(d)
# print(len(d))
