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
        usernamelayout = qtw.QHBoxLayout()
        usernamelayout.addWidget(username_label)
        usernamelayout.addWidget(username_input)
        
        passwordlayout = qtw.QHBoxLayout()
        passwordlayout.addWidget(password_label)
        passwordlayout.addWidget(password_input)
        
        layout = qtw.QVBoxLayout()
        layout.addLayout(usernamelayout)
        layout.addLayout(passwordlayout)
        
        self.setLayout(layout)
        
        #MY CODE ENDS HERE    
        self.show()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    w = MainWindow()    
    sys.exit(app.exec_())
    sys.exit()