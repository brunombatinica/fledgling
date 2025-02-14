#Simple tick tac toe with random computer moves
#Future plans - tkin, then website then algorithm to always win or tie

#make the playing board
#rows = [0]*3
#mat = list(rows for x in range(0,3))
    # Contructing playing grid
    # for x in range(3):
    #    for i in range(3):
    #        mat

import random

class tictactoe(object):
    #initialized as an empty board
    def __init__(self):
        #Empty board
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        #Valid move tracker
        self.valid = False
        #Win condition tracker
        self.movecount = 0
        self.end = False
        
        #Markers
        self.playermarker = "X"
        self.compmarker = "0"

    def printboard(self):
        for x in self.board:
            print(x)
        print("")
        
    #Define a way to alter the board
    def move(self,r,c,marker):
        if self.board[r-1][c-1] == " ":
            self.board[r-1][c-1] = marker
            self.valid = True
            self.movecount += 1
            self.printboard()
            self.check()
        else:
            pass
            
    #define move function
    def usermove(self):   
        self.valid = False
        while not self.valid:
            #get & test inputs ##############UNFINISHED
            r = int(input("what row? (1-3) "))
            c = int(input("what column? (1-3) "))

            self.move(r,c,"X") 
            
            if not self.valid:
                print("invalid move")
            
    #Define computer move
    def compmove(self):
        self.valid = False
        while not self.valid:
            r = random.randint(1,3)
            c = random.randint(1,3)
            
            self.move(r,c,self.compmarker)
            
    def compare(self,string):
        if string == "XXX" or string == "000":
            print("WHOOORAY!")
            self.end = 1
                
    def check(self):
        if self.movecount == 9:
            self.end = 1
        
        for i in self.board:
            if self.compare("".join(i)):
                self.end = 1
        
        test = ""
        for i in range(0,3):
            for j in range(0,3):
                test += self.board[j][i]
            print("verticals",test)
            self.compare(test)
            test = ""
        
        #lazy do it shit
        test = ""
        for j in range (0,3):
            test += self.board[j][j]
        self.compare(test)
        test = ""
        
        for j in range (0,3):
            test += self.board[j][2-j]
        self.compare(test)
        test = ""

game = tictactoe()
game.printboard()
while not game.end:
    game.usermove()
    game.compmove()



