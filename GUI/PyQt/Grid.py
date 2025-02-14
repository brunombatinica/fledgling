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

        #Create widgets
        username_label = qtw.QLabel("Username")
        password_label = qtw.QLabel("Password")
       
        username_input = qtw.QLineEdit()
        password_input = qtw.QLineEdit()
        password_input.setEchoMode(qtw.QLineEdit.Password)
       
        cancel_button = qtw.QPushButton('Cancel')
        submit_button = qtw.QPushButton("Login")
       
        # can nest layouts to get more complicatio
        layout = qtw.QGridLayout()
        layout.addWidget(username_label,0,0)
        layout.addWidget(username_input,0,1)
        layout.addWidget(password_label,1,0)
        layout.addWidget(password_input,1,1)
        
        self.setLayout(layout)
        
        #MY CODE ENDS HERE    
        self.show()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    w = MainWindow()    
    sys.exit(app.exec_())
    sys.exit()