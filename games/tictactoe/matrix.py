#Simple tick tac toe with random computer moves
#Future plans - tkin, then website then algorithm to always win or tie

#make the playing board
#rows = [0]*3
#mat = list(rows for x in range(0,3))
    # Contructing playing grid
    # for x in range(3):
    #    for i in range(3):
    #        mat

#define move function
def usermove():
    #set up global variables
    global y_in
    global x_in


    #get & test inputs ##############UNFINISHED
    y_in = int(input("what row? (1-3) ")) - 1
    x_in = int(input("what column? (1-3) ")) - 1

        #try:
        #     y_int = int(rawy) - 1
        #except TypeError:
        #    rawy = raw_input("what row? (1-3) ")

    #space for clarity
    print("")

#define board print function
def board(matrix):
    for x in matrix:
        print(x)
    print("")


#intialise board (for now)
mat = [[" "," "," "],[" "," "," "],[" "," "," "]]

#display board
board(mat)

#set up variables
win = False
move = 1
tt = ["X","O"]
import random
test = [[],[],[]]



#play move
while not win and move < 10:
    if move % 2 == 1:
        #ask for move (not robust)
        usermove()
    else:
        #computer move (random)
        y_in = random.randint(0,2)
        x_in = random.randint(0,2)

    #PERFROM MOVE
    row = mat[y_in][:]

    #test if valid move
    if row[x_in] == "X" or row[x_in] == "O":
        if move % 2 == 0:
            pass
        else:
            print("please input a valid move...")

    #Valid move
    else:
        #update row
        row[x_in] = tt[(move%2)]
        #use row to update matrix
        mat[y_in] = row[:]
        board(mat)
        move += 1

        #test for win
        for x in range(0,3):
            #check row
            if mat [x] == ["X","X","X"] or mat[x] == ["O","O","O"]:
                win = True
            else:
                pass

            #check column & diagnonal
            ### *** in future can transpose matrix and check row again

            #populate test variable
            for i in range (0,3):
                test[0].append(mat[i][x])
                test[1].append(mat[i][i]) #not good coding as this is checked 3 times!
                test[2].append(mat[2-i][i]) #not good coding as this is checked 3 times!

            #check test
            for i in range (0,3):
                if test[i] == ["X","X","X"] or test[i] == ["O","O","O"]:
                    win = True
                else:
                    pass
            #reset test
            test = [[],[],[]]

#print message:
if move == 10:
    print("Stalemate!")
elif move % 2 == 0:
    print("Congratulations!")
else:
    print("Unlucky!, try again next time")




#mat[y_in][x]

#play a random move

#check for victory
