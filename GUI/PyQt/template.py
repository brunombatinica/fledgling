import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore
from PyQt5 import QtGui

class MainWindow(qtw.QWidget):
    #Over write init method
    def __init__(self, *args, **kwargs):
        #pass all arguments to parent methods - allows all normal Qwidget behaviour to occur
        super().__init__(*args, **kwargs)
        #MY CODE WILL GO HERE

       

        #MY CODE ENDS HERE    
        self.show()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    w = MainWindow()    
    sys.exit(app.exec_())
    sys.exit()