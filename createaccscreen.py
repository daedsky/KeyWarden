# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_account_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QMessageBox
from qt_material import apply_stylesheet
from encrypt_decrypt import EncrypterDecrypter
from loginscreen import Ui_LoginScreen


class Ui_CreateAccScreen(object):
    def start_login_screen(self):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.LoginWindow.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
        self.loginui = Ui_LoginScreen()
        self.loginui.setupUi(self.LoginWindow)
        self.LoginWindow.show()

    def setupUi(self, CreateAccScreen):
        self.CREATEACCSCREEN = CreateAccScreen
        CreateAccScreen.setObjectName("CreateAccScreen")
        CreateAccScreen.setEnabled(True)
        CreateAccScreen.resize(350, 363)
        CreateAccScreen.setStyleSheet("")
        QFontDatabase.addApplicationFont('resources/fonts/Roboto.ttf')
        QFontDatabase.addApplicationFont('resources/fonts/Itim.ttf')
        self.centralwidget = QtWidgets.QWidget(CreateAccScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.pswd_input_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pswd_input_lineEdit.setGeometry(QtCore.QRect(25, 200, 300, 35))
        self.pswd_input_lineEdit.setStyleSheet("font-family:Itim;font-size:16px;")
        self.pswd_input_lineEdit.setObjectName("pswd_input_lineEdit")
        self.pswd_input_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.create_acc_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_acc_btn.setGeometry(QtCore.QRect(25, 290, 300, 50))
        self.create_acc_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_acc_btn.setObjectName("create_acc_btn")
        self.enter_your_pswd_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_your_pswd_label.setGeometry(QtCore.QRect(25, 160, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.enter_your_pswd_label.setFont(font)
        self.enter_your_pswd_label.setStyleSheet("")
        self.enter_your_pswd_label.setObjectName("enter_your_pswd_label")
        self.show_pswd_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.show_pswd_checkbox.setGeometry(QtCore.QRect(25, 250, 125, 17))
        self.show_pswd_checkbox.setStyleSheet("font-size:12px;")
        self.show_pswd_checkbox.setObjectName("show_pswd_checkbox")
        self.lock_img_label = QtWidgets.QLabel(self.centralwidget)
        self.lock_img_label.setGeometry(QtCore.QRect(0, 20, 101, 101))
        self.lock_img_label.setText("")
        self.lock_img_label.setPixmap(QtGui.QPixmap("resources/images/thelock.png"))
        self.lock_img_label.setObjectName("lock_img_label")
        self.key_warden_label = QtWidgets.QLabel(self.centralwidget)
        self.key_warden_label.setGeometry(QtCore.QRect(90, 45, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.key_warden_label.setFont(font)
        self.key_warden_label.setObjectName("key_warden_label")
        CreateAccScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateAccScreen)
        QtCore.QMetaObject.connectSlotsByName(CreateAccScreen)

    def retranslateUi(self, CreateAccScreen):
        _translate = QtCore.QCoreApplication.translate
        CreateAccScreen.setWindowTitle(_translate("CreateAccScreen", "KeyWarden - Create Account"))
        self.create_acc_btn.setText(_translate("CreateAccScreen", "Create"))
        self.enter_your_pswd_label.setText(_translate("CreateAccScreen", "Create Master Password"))
        self.show_pswd_checkbox.setText(_translate("CreateAccScreen", "show password"))
        self.key_warden_label.setText(_translate("CreateAccScreen", "KeyWarden"))

        self.show_pswd_checkbox.clicked.connect(self.showPswdFunction)

        self.create_acc_btn.clicked.connect(self.create_account)

    def showPswdFunction(self):
        if self.show_pswd_checkbox.isChecked():
            self.pswd_input_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            return
        self.pswd_input_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    def create_account(self):
        def popup():
            msgbox = QMessageBox()
            msgbox.setWindowTitle('Do you want to continue?')
            msgbox.setText('''Master password is the key to see all your saved passwords.
So, make sure you remember your master password.
If you forget it then you cannot restore it again and you will lose all your passwords stored in KeyWarden.
Click "Yes" if you can remember this password.''')
            msgbox.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
            msgbox.setIcon(QMessageBox.Warning)
            cancel_btn = msgbox.addButton(QMessageBox.Cancel)
            ok_btn = msgbox.addButton(QMessageBox.Yes)
            msgbox.exec_()
            return cancel_btn, ok_btn, msgbox.clickedButton()

        def isStrongPswd(pswd: str):
            l, u, s, d = 0, 0, 0, 0
            if len(pswd) >= 8:
                for x in pswd:
                    if x.islower():
                        l += 1
                    elif x.isupper():
                        u += 1
                    elif x.isdigit():
                        d += 1
                    elif x in "!@#$%^&*_|.?,":
                        s += 1

            if all([l, u, s, d]):
                return True
            else:
                return False

        if isStrongPswd(self.pswd_input_lineEdit.text()):
            cancel, ok, clicked_btn = popup()
            if clicked_btn == ok:
                master_pswd = self.pswd_input_lineEdit.text().encode()
                EncrypterDecrypter.create_master_pswd(master_pswd)
                def successpopup():
                    msgbox = QMessageBox()
                    msgbox.setWindowTitle("Success")
                    msgbox.setText("Successfully created Master Password")
                    msgbox.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
                    msgbox.setStyleSheet("color:#01937c")
                    msgbox.exec_()

                successpopup()
                self.start_login_screen()
                self.CREATEACCSCREEN.close()
                #self.creat_acc_screen.close()
            else:
                print("clicked cancel")
        else:
            box = QMessageBox()
            box.setWindowTitle('Weak password')
            box.setIcon(QMessageBox.Critical)
            box.setText("""Your password lenght must be at least 8 characters long
and must contain uppercase, lowercase, digits and symbols.""")
            box.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
            box.exec_()



if __name__ == "__main__":
    if os.path.isfile('resources/data/master_pswd.json'):
        app = QtWidgets.QApplication(sys.argv)
        apply_stylesheet(app, 'my_dark_lightblue.xml')
        LoginScreen = QtWidgets.QMainWindow()

        LoginScreen.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
        ui = Ui_LoginScreen()
        ui.setupUi(LoginScreen)
        LoginScreen.show()
        sys.exit(app.exec_())
    else:
        app = QtWidgets.QApplication(sys.argv)
        apply_stylesheet(app, 'my_dark_lightblue.xml')
        CreateAccScreen = QtWidgets.QMainWindow()
        CreateAccScreen.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
        ui = Ui_CreateAccScreen()
        ui.setupUi(CreateAccScreen)
        CreateAccScreen.show()
        sys.exit(app.exec_())
