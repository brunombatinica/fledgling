#THIS CODE IS GARBAGE









#code for generating list of all possible subset from an array
# try use nice recursive solution



# a = [1,2,3,4]


# def subset_gen(x):
#     #Recursive subsets generator

#     def mask(x,i):
#         a = [*x]
#         del(a[i])
#         return a


#     # Base Case
#     # set to 0 so include the null set
#     if len(x) == 1:
#         yield x
    
#     else:
#         yield x
#         for i in range(len(x)):
            

#         x.pop()
#         yield from subset_gen(x)
        



# b = [i for i in subset_gen(a)]
    
# print(b)





# ###############old method
#? use generators?????


# def mask(x,i):
#         #masks the ith element in array x
#         del(x[i])
#         return x

# def subsets(x):
#     #input an array and return list of all possible subset
#     def mask(x,i):
#         #masks the ith element in array x
#         a = [*x]
#         del(a[i])
#         return a

#     print("new call")

#     #base case
#     if len(x) == 1:
#         print("base case")
#         yield x
    
#     else:
#         yield x
        
#         for i in range(len(x)):
#             print(i,x)
#             yield from subsets(mask(x,i))


###################STILL WRONG
# def subset_gen(x):
#     #Recursive subsets generator

#     # Base Case
#     # set to 0 so include the null set
#     if len(x) == 1:
#         yield x
#     else:
#         for i in range(len(x)):
#             yield x[i:]
#         x.pop()
#         yield from subset_gen(x)