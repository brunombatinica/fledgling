import random

#initialize grid
l = [""]*10
mat = []
for i in range(0,10):
    mat.append(l[:])

#define board print function
def board(matrix):
    for x in range(len(matrix)):
        print matrix[x]
    print ""

mat[random.randint(0,9)][random.randint(0,9)] = 0

board(mat)
