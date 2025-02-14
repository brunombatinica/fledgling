# #Collatz sequence

# def collatz(n,hash_table):
#     #must be slow passing in the whole hash table each time


#     count = 1
#     while n != 1:
#         #print(n)
#         if n%2 == 1:
#             n = 3*n + 1
#         else:
#             n = n//2

#         count += 1
#     return count

# #print(collatz(13))

# # will probabiliy be odd
# # ? prime

# max = 1
# max_ind = None
# for i in range(1,1000000,2):
#     temp = collatz(i)
#     #print(max_ind)

#     if temp > max:
#         max_ind = i
#         max = temp

# print(max)
# print(max_ind)


# #MEMOIZATION MAKES THIS SO MUCH QUICKER WOWOOWOWOWWOOWOWO

def par_col(input):
    n = input
    count = 0
    while n >= input:
        if n == 1:
            return (count,n)
        if n%2 == 1:

            n = 3*n + 1
        else:
            n = n//2
        count += 1
    return (count,n)

memoization_hash = {1 : 1, 2: 2}
for i in range(3,1000000):
    count,n = par_col(i)
    memoization_hash[i] = count + memoization_hash[n]

#print(memoization_hash)
max = 1
max_ind = 0
for i in memoization_hash.items():
    if i[1] > max:
        max = i[1]
        max_ind = i[0]
print(max_ind)




