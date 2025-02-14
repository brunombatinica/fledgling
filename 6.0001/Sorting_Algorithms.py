# Simple illustration of sorting algorithsm

import random 
import time

def randlis(n):
    #n = 10
    l = []
    for i in range(n):
        l.append(random.randint(0,10))
    
    return l

def timefun(fun,inp):
    #times how long a function takes
    start = time.process_time()
    
    fun(inp)
    
    
    length = time.process_time() - start
    #add a fancy print statement
    print(length)
    
    return length
    


#bubble sort
def bubble(l):
    # sorts a list l
    
    solved = False
    steps = 0
    
    while not solved:
        #Check is a change has been made
        solved = True
        
        #increment counter
        steps += 1
        
        #run through list
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                #indicate not solved
                solved = False
                
                #swap elements
                l[i],l[i+1] = l[i+1],l[i]
                
        #print result
        print(l)
     
    print(steps)
    return l   
    
# def selection(l):
#     #sorts list l
#     #ABSOLUTE HORSESHIT CODE BY ME!
    
#     solved = False
#     steps = 0
    
#     for i,x in enumerate(l):
        
#         #initialize minimum value
#         min_val = x
#         min_ind = i
        
#         #find minimum element and index
#         for j in range(min_ind,len(l)):
#             if l[j] < min_val:
#                 min_val = l[j]
#                 min_ind = j
                
#             #increment steps
#             steps += 1
                
            
#         #replace index spot
#         l[i],l[min_ind] = min_val,l[i]
        
#         #debugging
#         print(l)
        

#     print(steps)
                
# def selection(l):
#     #So ineficcient copy and pasting everythig
#     prefix = []
#     suffix = [*l]
    
#     steps = 0
    
#     while len(prefix) != len(l):    
        
#         #initialize minimums
#         min_val = suffix[0]
#         min_ind = 0
        
#         #search suffix
#         for i in range(1,len(suffix)):
#             if suffix[i] < min_val:
#                 min_ind = i
#                 min_val = suffix[i]
                
#             steps +=1
#             print(prefix,suffix)
        
#         #move element
#         prefix.append(suffix.pop(min_ind))
        
#         # print(prefix)
#         # print("length:",len(prefix))
              
#     print(steps)
#     return prefix   

def selection(l):
    suffixind = 0
    steps = 0
    
    while suffixind != len(l):
        for i in range(suffixind,len(l)):
            if l[i]<l[suffixind]:
                #teh replaces it a number of times
                l[suffixind],l[i] = l[i],l[suffixind]
            print(l)
            steps += 1
        suffixind += 1
       
    return l

# def mergesort(l):
#     #TOO MUCH COPYING!
    
#     if len(l) <= 1:
#         return l
#     else:
#         #split list in 2
#         midpoint = len(l)//2
#         list1 = mergesort(l[:midpoint])
#         list2 = mergesort(l[midpoint:])
        
#         merged = []
        
#         while list1 != [] and list2 != []:
#             if list1[0] < list2[0]:
#                 merged.append(list1.pop(0))
#             else:
#                 merged.append(list2.pop(0))
                
                
#         #add remianing
#         merged = merged + list1 + list2
       
#         print(merged)
#         return merged
   

def merge(left,right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while (i < len(left)):
        result.append(left[i])
        i += 1
        
    while (j < len(right)):
        result.append(right[j])
        j += 1
      
    return result

def mergesort(L):
    
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergesort(L[:middle])
        right = mergesort(L[middle:])
        return merge(left, right)
    
    
    


     
random.seed(200)
l = randlis(10)
#bubble([*l])
#selection([*l])
mergesort([*l])