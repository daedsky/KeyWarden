from PyQt5 import QtWidgets, QtGui
from createaccscreen import Ui_CreateAccScreen
from loginscreen import Ui_LoginScreen
from qt_material import apply_stylesheet
import os
import sys

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
