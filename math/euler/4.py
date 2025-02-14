# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:02:51 2021

@author: Bbatd
"""

#project euler challenge #4
#palindromic number

'''
def ispalindrome(x):
    x = str(x)
    for i in range((len(x)//2)):
        if x[i] != x[-(1+i)]:
            return False
    return True
'''

def palindrome(s):
    if s == s[-1]:
        return True
    else:
        return False
    


'''
#this is not garunteed to return the largest one.....
for i in range(1000,1,-1):
    for j in range(1000,1,-1):
        if ispalindrome(i*j):
            print (f"i = {i}, j = {j} i*j
            break break
'''

# 3 methods
#1. Semi brute force
#2. use numpy to make a mesgrid of i and j and work through it diagnoally
#3. while loops
#4. break out of 1 string and test up
#5. ?recursion 

#math cheese - palindrome will alwasy be a multiple of 11, since 11 is a prime at least 1 of the factors will thus also be a multiple of 11
  

'''
#3.
i = 999
j = 999
pal = 0

while i*j >= pal:
    print("test")
    while i*j >= pal and not ispalindrome(i*j):
        print(i,j)
        j -= 1
    
    #kinda shit code here
    if ispalindrome(i*j):
        pal = i*j  
        
    print (f"i = {i}, j = {j}, pal = {pal}")
    j = i
    i -= 1
   
'''

pal = 0

for i in range(999,1,-1):
    for j in range(999,1,-1):
        if i*j < pal:
            break
        elif ispalindrome(i*j):
            pal = i*j
            break
    if i**2 < pal:
        break


print(pal)