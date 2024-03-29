# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from logIn_win import Ui_logIn_screen

class Ui_Welcome_screen(object):
    def openLogIn_Win(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_logIn_screen()
        self.ui.setupUi(self.window)
        self.window.show()
        
        
    def setupUi(self, Welcome_screen):
        Welcome_screen.setObjectName("Welcome_screen")
        Welcome_screen.resize(1248, 843)
        Welcome_screen.setStyleSheet("background-color: rgb(94, 94, 94)")
        self.widget = QtWidgets.QWidget(Welcome_screen)
        self.widget.setGeometry(QtCore.QRect(50, 20, 1181, 801))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(290, 50, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.logIn = QtWidgets.QPushButton(self.widget, clicked = lambda: self.openLogIn_Win())
        self.logIn.setGeometry(QtCore.QRect(370, 230, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.logIn.setFont(font)
        self.logIn.setStyleSheet("border-radius: 20px ;\n"
"background: rgb(255, 88, 91)")
        self.logIn.setObjectName("logIn")
        self.signUp = QtWidgets.QPushButton(self.widget)
        self.signUp.setGeometry(QtCore.QRect(370, 320, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signUp.setFont(font)
        self.signUp.setStyleSheet("border-radius: 20px ;\n"
"background: rgb(255, 88, 91)")
        self.signUp.setObjectName("signUp")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(890, 510, 401, 301))
        font = QtGui.QFont()
        font.setPointSize(109)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(-20, -30, 441, 311))
        font = QtGui.QFont()
        font.setPointSize(105)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.logIn.raise_()
        self.signUp.raise_()
        self.label_2.raise_()

        self.retranslateUi(Welcome_screen)
        QtCore.QMetaObject.connectSlotsByName(Welcome_screen)

    def retranslateUi(self, Welcome_screen):
        _translate = QtCore.QCoreApplication.translate
        Welcome_screen.setWindowTitle(_translate("Welcome_screen", "Dialog"))
        self.label.setText(_translate("Welcome_screen", "     AG ZONE -- LOG-IN OR SIGN UP"))
        self.logIn.setText(_translate("Welcome_screen", "LOG IN"))
        self.signUp.setText(_translate("Welcome_screen", "SIGN UP"))
        self.label_2.setText(_translate("Welcome_screen", "👨🏻‍🌾"))
        self.label_3.setText(_translate("Welcome_screen", "🌿"))


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Welcome_screen = QtWidgets.QDialog()
        ui = Ui_Welcome_screen()
        ui.setupUi(Welcome_screen)
        Welcome_screen.show()
        sys.exit(app.exec_())
