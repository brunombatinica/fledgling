#https://www.youtube.com/watch?v=5QpguaNFecQ&list=PLXlKT56RD3kBu2Wk6ajCTyBMkPIGx7O37&index=3

import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore
from PyQt5 import QtGui
#Imports a uic file into python - make sure you look at python documentation
from PyQt5 import uic

##Ui_########, baseClass = uic.loadUiType("############### name of ui.ui") #Returns tuple of 2 classes (form class, baseclass)

class MainWindow(baseClass):
    #Over write init method
    def __init__(self, *args, **kwargs):
        #pass all arguments to parent methods - allows all normal Qwidget behaviour to occur
        super().__init__(*args, **kwargs)
        #MY CODE WILL GO HERE
        self.ui = Ui_###########
        self.ui.setupUi(self)
       

        #MY CODE ENDS HERE    
        self.show()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv) 
    app.setQuitOnLastWindowClosed(True)
    w = MainWindow()    
    sys.exit(app.exec_())