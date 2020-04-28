
from PyQt5 import QtWidgets
import sys
from controller import MyApplication

def main():
    #
    # Setup the application and pass it any command line
    # arguments that might be present.
    #
    pyQtApp = QtWidgets.QApplication(sys.argv)
    #
    # Create a new window and show it to the user. Then
    # start the applications main event loop.
    #
    myApplication = MyApplication(pyQtApp)
    myApplication.show()

    exitCondition = pyQtApp.exec_()
    sys.exit(exitCondition)

def read_file():


if __name__ == '__main__':
    main()