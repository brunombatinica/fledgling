import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui

class MainWindow(qtw.QWidget):
    
    authenticated = qtc.pyqtSignal(str)
        
    #Over write init method
    def __init__(self, *args, **kwargs):
        #pass all arguments to parent methods - allows all normal Qwidget behaviour to occur
        super().__init__(*args, **kwargs)
        #MY CODE WILL GO HERE

        #Create widgets
        self.username_label = qtw.QLabel("Username")
        self.password_label = qtw.QLabel("Password")
       
        self.username_input = qtw.QLineEdit()
        self.password_input = qtw.QLineEdit()
        self.password_input.setEchoMode(qtw.QLineEdit.Password)
       
        self.cancel_button = qtw.QPushButton('Cancel')
        self.submit_button = qtw.QPushButton("Login")
       
        layout = qtw.QFormLayout()
        layout.addRow("User:", self.username_input)  
        layout.addRow("Password:", self.password_input) 
        
        #Button widget
        button_widget = qtw.QWidget()
        button_widget.setLayout(qtw.QHBoxLayout())
        #Dont ened to assign a name to the layout can just call the accesor funciton for the layout which is stored withing our new butto_widget widget
        button_widget.layout().addWidget(self.cancel_button)
        button_widget.layout().addWidget(self.submit_button)
        layout.addRow("",button_widget)
        
        #Button signals
        #Connect cancel button click to out widgets close
        self.cancel_button.clicked.connect(self.close)
        self.submit_button.clicked.connect(self.authenticate)
        
        self.authenticated.connect(self.user_logged_in)
        self.username_input.textChanged.connect(self.set_button_text)
            
        self.setLayout(layout)
        
        #MY CODE ENDS HERE    
        self.show()
        
    @qtc.pyqtSlot(str)    
    def set_button_text(self,text):
        if text:
            self.submit_button.setText("Log In {}".format(text))

        else:
            self.submit_button.setText("Log in")
        
        
    def authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "user" and password == "password":
            qtw.QMessageBox.information(self, "SUccess","you are logged int")                     
            self.authenticated.emit(username)   
        else:
            qtw.QMessageBox.critical(self,"Failed","You are not logged in")
        
    def user_logged_in(self, username):
         qtw.QMessageBox.information(self, "Logged in", "{} is logged in".format(username))
            
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    w = MainWindow()    
    sys.exit(app.exec_())
    sys.exit()