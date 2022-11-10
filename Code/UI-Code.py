import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget

import sqlite3

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcome_screen.ui",self)
        self.logIn.clicked.connect(self.gotologIn)
        self.signUp.clicked.connect(self.gotosignUp)

    def gotologIn(self):
        logIn = logInScreen()
        widget.addWidget(logIn)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotosignUp(self):
        signUp = signUpAccScreen()
        widget.addWidget(signUp)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class logInScreen(QDialog):
    def __init__(self):
        super(logInScreen, self).__init__()
        loadUi("logIn.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.logIn.clicked.connect(self.logInfunction)

    def logInfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("Please input all fields.")

        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()
            query = 'SELECT password FROM logIn_info WHERE username =\''+user+"\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == password:
                print("Successfully logged in.")
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")

class signUpAccScreen(QDialog):
    def __init__(self):
        super(signUpAccScreen, self).__init__()
        loadUi("signU.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)

    def signupfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error.setText("Please fill in all inputs.")

        elif password!=confirmpassword:   # != = ! + =
            self.error.setText("Passwords do not match.")
        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()

            user_info = [user, password]
            cur.execute('INSERT INTO logIn_info (username, password) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()

            fillprofile = FillProfileScreen()
            widget.addWidget(fillprofile)
            widget.setCurrentIndex(widget.currentIndex()+1)
        
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("EXITING APP . . .")