# Towers of Hanoi 
# Matrix display

#define board print function (OHH BABY SO PYTHONIC)
#prints the transposed nested list
def board(matrix):
    matrix = T(matrix)
    for x in matrix:
        print(x)
    print("") # space for clarity


#define transpose function - will be easier to work with
def T(matrix):
    output = [] 
    for i in range(len(matrix[0])):
        output.append([j[i] for j in matrix ] )        
        
    return output
  
#defines the manual move
def man_move(matrix):
    #input pick up piece########################################
    colindex1 = int(input("pick up piece from column... (1-3) ? ")) - 1
    col1 = mat[colindex1]
    #Test if valid (not empty)
    while index(col1) == height:
        colindex1 = int(input("Please pick a valid column... (1-3) ? ")) - 1  
        col1 = mat[colindex1]
        
    #Pick up piece
    piece = col1[index(col1)]
    col1[index(col1)] = " "
        
    #input place piece########################################
    colindex2 = int(input("place piece in column... (1-3) ? ")) - 1 
    #Test if same columns picked
    if colindex2 == colindex1:
        col1[index(col1)-1] = piece
        return matrix
    #test if valid
    col2 = mat[colindex2]
    
    #While not empty row selected test if valid
    while index(col2) < height:
        print(int(col2[index(col2)]))
        if int(col2[index(col2)]) > int(piece):
            break
        else: 
            colindex2 = int(input("Please pick a valid column (1-3 ...")) - 1 
            col2 = mat[colindex2]
            #Test if same columns picked
            if colindex2 == colindex1:
                col1[index(col1)-1] = piece
                return matrix
    
    col2[index(col2) - 1] = piece
    
    #Work out spare column
    colindex3 = 3 - colindex1 - colindex2
    
    #Reconstruct the matrix
    output = [[],[],[]]
    output[colindex1] = col1
    output[colindex2] = col2
    output[colindex3] = matrix[colindex3]
    
    return output  
       
#Not robust needs valid moves
def auto_move(matrix,fr,to):
    #input pick up piece########################################
    colindex1 = fr - 1
    col1 = mat[colindex1]
        
    #Pick up piece
    piece = col1[index(col1)]
    col1[index(col1)] = " "
        
    #input place piece########################################
    colindex2 = to - 1
    col2 = mat[colindex2]    
    col2[index(col2) - 1] = piece
    
    # Work out left over column (previously done with remove functions)
    colindex3 = 3 - colindex1 - colindex2
    
    #Reconstruct the matrix
    output = [[],[],[]]
    output[colindex1] = col1
    output[colindex2] = col2
    output[colindex3] = matrix[colindex3]
    
    return output

def index(array):   
    # nice piece of code  
    # return index of first non " " term, else return False       
    return next((i for i,x in enumerate(array) if x != " "), height)
 
#Solver using recursion
def Towers(n,fr,to,spare):
    a = []
    if n == 1:
        print(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
    return(a)


#SOlution generator
def Solution(n,fr,to,spare):
    a = []
    if n == 1:
        return([fr,to])
    else:
        a = a + Solution(n-1,fr,spare,to)
        a = a + Solution(1,fr,to,spare)
        a = a + Solution(n-1,spare,to,fr)
    return a

#Alternative definintion with n == 0 base case
def Solution2(n,fr,to,spare):
    a = []
    if n == 0:
        pass
    else:
        a = a + Solution(n-1,fr,spare,to)
        a = a + [fr,to]
        a = a + Solution(n-1,spare,to,fr)
    return a
    
#intialise board (for now)
height = 3
col = [" "]*height
mat = [col[:] for _ in range(3)]
#Define initial tower 
for i,x in enumerate(mat[0]):
    mat[0][i] = str(i+1)


win = False
#Crude move counter
i = 0
board(mat)
#board(auto_move(mat,1,3))
Towers(height,1,3,2)
moves = Solution(height,1,3,2)
print(moves)

for i in range(0,len(moves),2):
    mat = auto_move(mat,moves[i],moves[i+1]) 
    board(mat)
   
# Manual game...    
# while i < 10 and not win:
#     mat = man_move(mat)
#     board(mat)
#     i += 1





               
    


