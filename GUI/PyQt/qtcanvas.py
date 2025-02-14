import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QMainWindow):
    
    def __init__(self):
        #main window constructor
        super().__init__()
        #main UI code goes here
        
        # self.painter = qtg.QPainter()
        # self.setCentralWidget(self.painter) #can be any widget
    
        #################THIS IS BROCKEN
        
        #End main UI code
        self.show()
        
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())

