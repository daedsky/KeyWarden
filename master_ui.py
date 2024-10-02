import os
import clipboard
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QFileDialog
from qt_material import apply_stylesheet
import csv_editor
import encrypt_decrypt
from encrypt_decrypt import EncrypterDecrypter
from password_generator import generate


class InvalidHeaderError(Exception):
    pass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, masterpassword):
        self.MasterPswdFormDialog = b''
        self.masterpassword = masterpassword
        self.mainwindow = MainWindow
        QFontDatabase.addApplicationFont('resources/fonts/RobotoBold.ttf')
        QFontDatabase.addApplicationFont('resources/fonts/Itim.ttf')
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 811, 611))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")

        self.passwords_tab = QtWidgets.QWidget()
        self.passwords_tab.setObjectName("passwords_tab")

        self.scrollArea = QtWidgets.QScrollArea(self.passwords_tab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 0, 800, 595))
        self.scrollArea.setWidgetResizable(True)

        self.tabWidget.addTab(self.passwords_tab, "")

        self.add_new_tab = QtWidgets.QWidget()
        self.add_new_tab.setObjectName("add_new_tab")

        self.WebsiteLabel = QtWidgets.QLabel(self.add_new_tab)
        self.WebsiteLabel.setGeometry(QtCore.QRect(30, 178, 81, 41))
        self.WebsiteLabel.setStyleSheet("font-size:16px")
        self.WebsiteLabel.setObjectName("WebsiteLabel")

        self.LoginLabel = QtWidgets.QLabel(self.add_new_tab)
        self.LoginLabel.setGeometry(QtCore.QRect(30, 238, 81, 41))
        self.LoginLabel.setStyleSheet("font-size:16px;")
        self.LoginLabel.setObjectName("LoginLabel")

        self.PasswordLabel = QtWidgets.QLabel(self.add_new_tab)
        self.PasswordLabel.setGeometry(QtCore.QRect(30, 293, 81, 41))
        self.PasswordLabel.setStyleSheet("font-size:16px;")
        self.PasswordLabel.setObjectName("PasswordLabel")

        self.website_lineEdit = QtWidgets.QLineEdit(self.add_new_tab)
        self.website_lineEdit.setGeometry(QtCore.QRect(130, 175, 285, 40))
        self.website_lineEdit.setMaxLength(100)
        self.website_lineEdit.setFrame(False)
        self.website_lineEdit.setStyleSheet('font-family:Itim;font-size:14px;')
        self.website_lineEdit.setObjectName("website_lineEdit")

        self.login_lineEdit = QtWidgets.QLineEdit(self.add_new_tab)
        self.login_lineEdit.setGeometry(QtCore.QRect(130, 235, 285, 40))
        self.login_lineEdit.setInputMask("")
        self.login_lineEdit.setMaxLength(100)
        self.login_lineEdit.setStyleSheet("font-family:Itim; font-size:14px")
        self.login_lineEdit.setObjectName("login_lineEdit")

        self.password_lineEdit = QtWidgets.QLineEdit(self.add_new_tab)
        self.password_lineEdit.setGeometry(QtCore.QRect(130, 295, 285, 40))
        self.password_lineEdit.setMaxLength(100)
        self.password_lineEdit.setStyleSheet('font-family:Itim; font-size:14px;')
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.save_btn = QtWidgets.QPushButton(self.add_new_tab)
        self.save_btn.setGeometry(QtCore.QRect(183, 370, 91, 41))
        self.save_btn.setObjectName("save_btn")

        self.LockImgLabel = QtWidgets.QLabel(self.add_new_tab)
        self.LockImgLabel.setGeometry(QtCore.QRect(40, 40, 141, 101))
        self.LockImgLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LockImgLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LockImgLabel.setText("")
        self.LockImgLabel.setPixmap(QtGui.QPixmap("resources/images/lock_resized.png"))
        self.LockImgLabel.setObjectName("LockImgLabel")

        self.KeyWardenLabel = QtWidgets.QLabel(self.add_new_tab)
        self.KeyWardenLabel.setGeometry(QtCore.QRect(170, 85, 151, 41))
        self.KeyWardenLabel.setStyleSheet("font-family:RobotoBold;font-size:24px;font-weight:bold;")
        self.KeyWardenLabel.setObjectName("KeyWardenLabel")

        self.tabWidget.addTab(self.add_new_tab, "")
        self.generator_tab = QtWidgets.QWidget()
        self.generator_tab.setObjectName("generator_tab")

        self.horizontalSlider = QtWidgets.QSlider(self.generator_tab)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 260, 360, 21))
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setMinimum(4)
        self.horizontalSlider.setMaximum(80)
        self.horizontalSlider.setProperty("value", 16)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.GeneratePswdLineEdit = QtWidgets.QLineEdit(self.generator_tab)
        self.GeneratePswdLineEdit.setGeometry(QtCore.QRect(20, 120, 331, 31))
        self.GeneratePswdLineEdit.setText("")
        self.GeneratePswdLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.GeneratePswdLineEdit.setDragEnabled(False)
        self.GeneratePswdLineEdit.setReadOnly(True)
        self.GeneratePswdLineEdit.setPlaceholderText("")
        self.GeneratePswdLineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.GeneratePswdLineEdit.setClearButtonEnabled(False)
        self.GeneratePswdLineEdit.setStyleSheet("font-family:Itim;font-size:18px;")
        self.GeneratePswdLineEdit.setObjectName("GeneratePswdLineEdit")

        self.lengthLabel = QtWidgets.QLabel(self.generator_tab)
        self.lengthLabel.setGeometry(QtCore.QRect(50, 230, 81, 21))
        self.lengthLabel.setObjectName("lengthLabel")

        self.letters_checkbox = QtWidgets.QCheckBox(self.generator_tab)
        self.letters_checkbox.setGeometry(QtCore.QRect(100, 320, 111, 31))
        self.letters_checkbox.setObjectName("letters_checkbox")

        self.digits_checkbox = QtWidgets.QCheckBox(self.generator_tab)
        self.digits_checkbox.setGeometry(QtCore.QRect(100, 350, 101, 17))
        self.digits_checkbox.setObjectName("digits_checkbox")

        self.symbols_checkbox = QtWidgets.QCheckBox(self.generator_tab)
        self.symbols_checkbox.setGeometry(QtCore.QRect(100, 370, 141, 17))
        self.symbols_checkbox.setObjectName("symbols_checkbox")

        self.copy_btn = QtWidgets.QPushButton(self.generator_tab)
        self.copy_btn.setGeometry(QtCore.QRect(160, 160, 75, 31))
        self.copy_btn.clicked.connect(self.copyGeneratedPassword)
        self.copy_btn.setObjectName("copy_btn")

        self.refresth_btn = QtWidgets.QPushButton(self.generator_tab)
        self.refresth_btn.setGeometry(QtCore.QRect(360, 115, 51, 31))
        self.refresth_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/images/refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresth_btn.setIcon(icon)
        self.refresth_btn.setIconSize(QtCore.QSize(16, 16))
        self.refresth_btn.setShortcut("")
        self.refresth_btn.setCheckable(False)
        self.refresth_btn.setChecked(False)
        self.refresth_btn.setAutoRepeat(False)
        self.refresth_btn.setAutoDefault(False)
        self.refresth_btn.setDefault(False)
        self.refresth_btn.setFlat(False)
        self.refresth_btn.setObjectName("refresth_btn")

        self.min_label = QtWidgets.QLabel(self.generator_tab)
        self.min_label.setGeometry(QtCore.QRect(50, 280, 16, 16))
        self.min_label.setObjectName("min_label")

        self.max_label = QtWidgets.QLabel(self.generator_tab)
        self.max_label.setGeometry(QtCore.QRect(395, 280, 21, 16))
        self.max_label.setObjectName("max_label")

        self.tabWidget.addTab(self.generator_tab, "")

        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.tabWidget.addTab(self.settings_tab, "")

        self.importBtn = QtWidgets.QPushButton('import passwords', self.settings_tab)
        self.importBtn.setGeometry(90, 10, 160, 25)
        self.importBtn.clicked.connect(self.importPasswords)

        self.exportBtn = QtWidgets.QPushButton('export passwords', self.settings_tab)
        self.exportBtn.setGeometry(90, 60, 160, 25)
        self.exportBtn.clicked.connect(self.exportPasswords)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KeyWarden"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.passwords_tab), _translate("MainWindow", "Passwords"))
        self.WebsiteLabel.setText(_translate("MainWindow", "Website"))
        self.LoginLabel.setText(_translate("MainWindow", "Login"))
        self.PasswordLabel.setText(_translate("MainWindow", "Password"))
        self.website_lineEdit.setPlaceholderText(_translate("MainWindow", "Add URL... (eg: www.example.com)"))
        self.login_lineEdit.setPlaceholderText(_translate("MainWindow", "Add login... (eg: example@example.com)"))
        self.password_lineEdit.setPlaceholderText(_translate("MainWindow", "Add password..."))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.KeyWardenLabel.setText(_translate("MainWindow", "KeyWarden"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_new_tab), _translate("MainWindow", "Add new"))
        self.lengthLabel.setText(_translate("MainWindow", "length (16)"))
        self.letters_checkbox.setText(_translate("MainWindow", "Letters (eg: Aa)"))
        self.digits_checkbox.setText(_translate("MainWindow", "Digits (eg: 234)"))
        self.symbols_checkbox.setText(_translate("MainWindow", "Symbols (eg: !@#$%?..|)"))
        self.copy_btn.setText(_translate("MainWindow", "Copy"))
        self.min_label.setText(_translate("MainWindow", "4"))
        self.max_label.setText(_translate("MainWindow", "80"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generator_tab), _translate("MainWindow", "Generator"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.notes_tab), _translate("MainWindow", "Notes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("MainWindow", "Settings"))

        self.letters_checkbox.setChecked(True)
        self.digits_checkbox.setChecked(True)
        self.symbols_checkbox.setChecked(True)

        self.horizontalSlider.sliderMoved.connect(self.OnSliderMoved)
        self.horizontalSlider.sliderReleased.connect(self.OnSliderReleased)

        self.generate_new_password()

        self.refresth_btn.clicked.connect(self.generate_new_password)

        self.tabWidget.currentChanged.connect(self.resizeWindowAccordingToAddTab)

        self.addItemsToPassowdTab()

        self.save_btn.clicked.connect(self.addPassword)

    def showEnterMasterPswdDialog(self):
        def showPassword():
            if show_pswd_checkbox.isChecked():
                lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            else:
                lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        def ProceedFunction():
            self.MasterPswdFormDialog = lineEdit.text().encode()
            masterPswdDialog.close()

        width, height = self.getScreenResolution()
        x = int(width/3)
        y = int(height/4)

        masterPswdDialog = QtWidgets.QDialog()
        masterPswdDialog.setGeometry(x, y, 350, 363)
        masterPswdDialog.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
        masterPswdDialog.setWindowTitle("KeyWarden - Enter Master Password")

        lockimg = QtWidgets.QLabel('', masterPswdDialog)
        lockimg.setPixmap(QtGui.QPixmap('resources/images/thelock.png'))
        lockimg.setGeometry(0, 20, 101, 101)

        keyWardenLabel = QtWidgets.QLabel('KeyWarden', masterPswdDialog)
        keyWardenLabel.setGeometry(90, 45, 151, 61)
        keyWardenLabel.setStyleSheet("font-family:RobotoBold;font-size:16px;")

        enterMasterPswdLabel = QtWidgets.QLabel('Enter Master Password', masterPswdDialog)
        enterMasterPswdLabel.setGeometry(25, 160, 291, 31)
        enterMasterPswdLabel.setStyleSheet("font-family:RobotoBold;font-size:16px;font-weight:bold;")

        lineEdit = QtWidgets.QLineEdit(masterPswdDialog)
        lineEdit.setGeometry(25, 200, 300, 35)
        lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        lineEdit.setStyleSheet("font-family:Itim;font-size:14px;")

        show_pswd_checkbox = QtWidgets.QCheckBox('show password', masterPswdDialog)
        show_pswd_checkbox.setGeometry(25, 250, 125, 17)
        show_pswd_checkbox.setStyleSheet('font-size:12px;')
        show_pswd_checkbox.clicked.connect(showPassword)

        proceedBtn = QtWidgets.QPushButton('Proceed', masterPswdDialog)
        proceedBtn.setGeometry(25, 290, 300, 50)
        proceedBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        proceedBtn.clicked.connect(ProceedFunction)

        masterPswdDialog.exec_()

    def showPopup(self, title, desc, icon=None):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle(title)
        msgbox.setText(desc)
        if icon:
            msgbox.setIcon(icon)
        msgbox.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
        msgbox.exec_()

    @staticmethod
    def getScreenResolution():
        desktop = QtWidgets.QApplication.desktop()
        resoulution = desktop.screenGeometry()
        height = resoulution.height()
        width = resoulution.width()
        return width, height

    def importPasswords(self):
        try:
            # creates a popup to enter master password to verify
            # and sets "self.MasterPswdFromEnterMasterPswdScreen"
            self.showEnterMasterPswdDialog()

            MasterPswd = self.MasterPswdFormDialog

            if MasterPswd == b'' or MasterPswd == '':
                return

            # try to decrypt the token
            # if failed incorrect password popup will open
            token = EncrypterDecrypter.read_json('resources/data/master_pswd.json')['token']
            EncrypterDecrypter.decrypt(MasterPswd, token.encode())

            # open the csv file from where to import the passwords
            file, _ = QFileDialog().getOpenFileName(self.settings_tab, 'open file', 'c:/users/admin/documents',
                                                    'csv files (*.csv)')
            # if the path of file is not choosen
            if file == '':
                return

            f, data = csv_editor.read_csv(file)

            for i, x in enumerate(data):
                url = x.get('url')
                login = x.get('login')
                pswd = x.get('password')

                if any((url is None, login is None, pswd is None)):  # if any of them is none it means
                    raise InvalidHeaderError(
                        'Invalid Headers in csv file. valid headers are: "url", "login" and "password"')

                # conver the master pswd to hash using the master password
                pswd = EncrypterDecrypter.encrypt(MasterPswd, pswd.encode()).decode()

                # append the file with encrypted pswd
                csv_editor.append_csv('resources/data/credentials.csv', [url, login, pswd])

            f.close()
            self.deleteAllItemsOfPswdTabGroupBox()
            self.addItemsToPassowdTab()
            self.showPopup('success', 'successfully imported all passwords')

        except encrypt_decrypt.IncorrectPasswordError:
            self.showPopup("Incorrect Password", "Incorrect password! Please check the password and try again.",
                           QtWidgets.QMessageBox.Critical)

        except InvalidHeaderError:
            self.showPopup("Invalid headers",
                           'The file contains invalid headers. Valid header are: "url", "login" and "password"',
                           QtWidgets.QMessageBox.Critical)

    def exportPasswords(self):
        try:
            # creates a popup to enter master password to verify
            # and sets "self.MasterPswdFromEnterMasterPswdScreen"
            self.showEnterMasterPswdDialog()

            MasterPswd = self.MasterPswdFormDialog

            if MasterPswd == b'' or MasterPswd == '':
                return

            # try to decrypt the token
            # if failed incorrect password popup will open
            token = EncrypterDecrypter.read_json('resources/data/master_pswd.json')['token']
            EncrypterDecrypter.decrypt(MasterPswd, token.encode())

            file, data = csv_editor.read_csv('resources/data/credentials.csv')

            fp, _ = QFileDialog().getSaveFileName(self.settings_tab, 'csv files',
                                                  f'c:\\users\\{os.getlogin()}\\documents\\credentials.csv',
                                                  'csv files (*.csv)')

            if fp == '':
                return

            csv_editor.create_empty_csv(fp, ['url', 'login', 'password'])

            for i in data:
                url = i.get('website')
                login = i.get('login')
                password = i.get('password')
                real_pswd = EncrypterDecrypter.decrypt(MasterPswd, password.encode())
                csv_editor.append_csv(fp, [url, login, real_pswd])

            file.close()
            self.showPopup("exported", "password successfully exported.")

        except encrypt_decrypt.IncorrectPasswordError:
            self.showPopup("Incorrect Password", "Incorrect password! Please check the password and try again.",
                           QtWidgets.QMessageBox.Critical)

    def addItemsToPassowdTab(self):
        if not os.path.isfile('resources/data/credentials.csv'):
            return

        self.__formLayout = QtWidgets.QFormLayout()

        def createLayout():
            website = QtWidgets.QLineEdit("Website")
            website.setReadOnly(True)
            website.setStyleSheet("background-color:transparent;color:#DEE6E9;border:none;font-size:16px;")

            login = QtWidgets.QLineEdit("Login")
            login.setReadOnly(True)
            login.setStyleSheet("font-size:16px;background-color:transparent;color:#DEE6E9;border:none;")

            password = QtWidgets.QLineEdit("Passwords")
            password.setReadOnly(True)
            password.setStyleSheet("font-size:16px;background-color:transparent;color:#DEE6E9;border:none;")

            btn = QtWidgets.QPushButton(QtGui.QIcon('resources/images/noicon.png'), '')
            btn.setStyleSheet('''QPushButton{background-color:transparent;border:none}
                    PushButton::pressed{background-color:transparent}''')

            btn2 = QtWidgets.QPushButton(QtGui.QIcon('resources/images/noicon.png'), '')
            btn2.setStyleSheet('''QPushButton{background-color:transparent; border:none;}
                    QPushButton::pressed{background-color:transparent}''')

            hboxLayout = QtWidgets.QHBoxLayout()
            hboxLayout.addWidget(website)
            hboxLayout.addWidget(login)
            hboxLayout.addWidget(password)
            hboxLayout.addWidget(btn)
            hboxLayout.addWidget(btn2)

            return hboxLayout

        self.__formLayout.addRow(createLayout())

        file, data = csv_editor.read_csv('resources/data/credentials.csv')
        for i in data:
            self.__hboxlayout = QtWidgets.QHBoxLayout()

            self.__siteLineEdit = QtWidgets.QLineEdit()
            self.__siteLineEdit.setReadOnly(True)
            self.__siteLineEdit.setText(i.get('website'))
            self.__hboxlayout.addWidget(self.__siteLineEdit)

            self.__loginLineEdit = QtWidgets.QLineEdit()
            self.__loginLineEdit.setReadOnly(True)
            self.__loginLineEdit.setText(i.get('login'))
            self.__hboxlayout.addWidget(self.__loginLineEdit)

            self.__pswdLineEdit = QtWidgets.QLineEdit()
            self.__pswdLineEdit.setReadOnly(True)
            real_pswd = EncrypterDecrypter.decrypt(self.masterpassword, i.get('password').encode())
            self.__pswdLineEdit.setText(real_pswd)
            self.__pswdLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.__hboxlayout.addWidget(self.__pswdLineEdit)

            self.__showbtn = QtWidgets.QPushButton(QtGui.QIcon('resources/images/hide.png'), "")
            self.__showbtn.clicked.connect(self.showPassword)
            self.__hboxlayout.addWidget(self.__showbtn)

            self.__copybtn = QtWidgets.QPushButton(QtGui.QIcon('resources/images/copy.png'), "")
            self.__copybtn.clicked.connect(self.copyPassword)
            self.__hboxlayout.addWidget(self.__copybtn)

            self.__formLayout.addRow(self.__hboxlayout)

        file.close()

        self.__groupbox = QtWidgets.QGroupBox('Your Passwords')
        self.__groupbox.setLayout(self.__formLayout)

        self.scrollArea.setWidgetResizable(True)

        self.scrollArea.setWidget(self.__groupbox)

    def deleteAllItemsOfPswdTabGroupBox(self):
        try:
            layout = self.__groupbox.layout()
            for i in range(layout.rowCount()):
                row = layout.itemAt(i)
                for x in range(5):
                    widget = row.itemAt(x).widget()
                    widget.deleteLater()
                row.deleteLater()

            layout.deleteLater()
            self.__groupbox.deleteLater()

        except AttributeError:
            pass

    def addPassword(self):
        def popup(title, text, icon=None):
            msgbox = QtWidgets.QMessageBox()
            msgbox.setWindowTitle(title)
            msgbox.setText(text)
            msgbox.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
            if icon:
                msgbox.setIcon(icon)
            msgbox.exec_()

        web = self.website_lineEdit.text()
        login = self.login_lineEdit.text()
        pswd = self.password_lineEdit.text()
        encrypted_pswd = EncrypterDecrypter.encrypt(self.masterpassword, pswd.encode()).decode()
        if all([web, login, pswd]):
            if not os.path.isfile('resources/data/credentials.csv'):
                csv_editor.create_empty_csv('resources/data/credentials.csv', ['website', 'login', 'password'])
                csv_editor.append_csv('resources/data/credentials.csv', [web, login, encrypted_pswd])
                popup("success", "Password added to database.")
            else:
                csv_editor.append_csv('resources/data/credentials.csv', [web, login, encrypted_pswd])
                popup("success", "Password added to database.")

            self.website_lineEdit.setText("")
            self.login_lineEdit.setText("")
            self.password_lineEdit.setText("")
            self.deleteAllItemsOfPswdTabGroupBox()
            self.addItemsToPassowdTab()
        else:
            popup("Invalid credentials", "Please fill in all forms", QtWidgets.QMessageBox.Critical)

    def showPassword(self):
        obj = QtCore.QObject()
        btn = obj.sender()
        for i in range(1, self.__formLayout.rowCount()):
            show_btn = self.__formLayout.itemAt(i).itemAt(3).widget()
            if btn == show_btn:
                line_edit = self.__formLayout.itemAt(i).itemAt(2).widget()
                if line_edit.echoMode() == 2:
                    line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
                    show_btn.setIcon(QtGui.QIcon('resources/images/show.png'))
                    break
                else:
                    line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
                    show_btn.setIcon(QtGui.QIcon('resources/images/hide.png'))
                    break

    def copyPassword(self):
        obj = QtCore.QObject()
        btn = obj.sender()

        for i in range(self.__formLayout.rowCount()):
            copyBtn = self.__formLayout.itemAt(i).itemAt(4).widget()
            if btn == copyBtn:
                pswd = self.__formLayout.itemAt(i).itemAt(2).widget().text()
                clipboard.copy(pswd)

                msgbox = QtWidgets.QMessageBox()
                msgbox.setText("successfully copied password to clipboard.")
                msgbox.setWindowTitle("Success")
                msgbox.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
                msgbox.exec_()

                break

    def resizeWindowAccordingToAddTab(self):
        if self.tabWidget.currentIndex() == 0:
            self.mainwindow.resize(800, 611)
        elif self.tabWidget.currentIndex() == 1:
            self.mainwindow.resize(428, 594)
        elif self.tabWidget.currentIndex() == 2:
            self.mainwindow.resize(428, 594)
        elif self.tabWidget.currentIndex() == 3:
            self.mainwindow.resize(350, 350)

    def copyGeneratedPassword(self):
        pswd = self.GeneratePswdLineEdit.text()
        clipboard.copy(pswd)

        msgbox = QtWidgets.QMessageBox()
        msgbox.setText("successfully copied password to clipboard.")
        msgbox.setWindowTitle("Success")
        msgbox.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
        msgbox.exec_()

    def OnSliderMoved(self):
        lenght = str(self.horizontalSlider.value())
        self.lengthLabel.setText(f"length ( {lenght} )")

    def OnSliderReleased(self):
        lenght = str(self.horizontalSlider.value())
        self.lengthLabel.setText(f"length ( {lenght} )")

    def generate_new_password(self):
        pswd = generate(length=self.horizontalSlider.value(),
                        letters=self.letters_checkbox.isChecked(),
                        _digits=self.digits_checkbox.isChecked(),
                        symbols=self.symbols_checkbox.isChecked())
        self.GeneratePswdLineEdit.setText(pswd)


# #27c93f noice
# #4063D8 blue noice
# #84E98A op green

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    apply_stylesheet(app, 'my_dark_lightblue.xml')

    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('resources/images/lockicon.png'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, "#HelloWorld12345".encode())
    MainWindow.show()
    sys.exit(app.exec_())
