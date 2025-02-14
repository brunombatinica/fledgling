import sys
import random

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui

#very bodged


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
            print("Horizontals",i)
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




class GameButton(qtw.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)                
        self.x = 0
        self.y = 0
        self.value = " "
    
    def update(self,x,y,value):
        self.x = x
        self.y = y
        self.setText(value)

class MainWindow(qtw.QWidget):      
    #Over write init method
    def __init__(self, *args, **kwargs):
        #pass all arguments to parent methods - allows all normal Qwidget behaviour to occur
        super().__init__(*args, **kwargs)
        #MY CODE WILL GO HERE
        
        #Set title
        self.setWindowTitle("Tic Tac Toe")
        #Set geometry
        self.setGeometry(100,100,300,500)
        
        layout = qtw.QGridLayout()
        
        #May be even smarter to use a dictionary...
        Button_List = []
        Button = GameButton()
        
        for i in range(1,4):
            for j in range(1,4): 
                button = GameButton()
                button.update(i,j,str(3*(i-1) + j))
                layout.addWidget(button,i,j)
                Button_List.append(button)
        
        Button_List[2].update(5,5,"SLut")
        
        self.setLayout(layout)
        #MY CODE ENDS HERE    
        self.show()
    
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    w = MainWindow()    
    sys.exit(app.exec_())
    sys.exit()
    
game = tictactoe()
game.printboard()
while not game.end:
    game.usermove()
    game.compmove()
