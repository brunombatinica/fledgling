from sympy import subsets


a = [1,2,3,4]

subset_list = [] 

def add_element(x,i):
    temp = [*x]

    if len(x) == 0:
        output = [i]
    else:
        output = [*x,i]


    for element in temp:
        if type(element) == int:
            output.append([element,i])
        elif type(element) == list: 
            output.append([*element,i])

    return output
        

# for i in a:
#     print(i,subset_list)
#     subset_list = add_element(subset_list,i)



# done recursively

def recsubsets(x):
    if len(x) == 1:
        return x
    
    else:
        a = x.pop()
        output = add_element(recsubsets(x),a)
        return output

print(recsubsets(a))


# def append_list(x,i):
    
#     if len(x) == 0:
#         return []
#     else:
#         output = []
#         for element in x:
#             if type(element) == int:
#                 output.append([element,i])
#             elif type(element) == list:
#                 output.append([*element,i])
#         return output

# for i in a:
#     temp = subset_list
#     subset_list.append(i)




