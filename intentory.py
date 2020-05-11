import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from time import sleep
from view import Scene

class Inventory(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Inventory, self).__init__(parent)

        self.setup_window()


    def setup_window(self):
        xSize = 1400
        ySize = 800
        self.setFixedSize(QSize(xSize, ySize))

        #
        # Starting coordinates of the window. This centers it on the desktop. Optional.
        #
        desktop = QtWidgets.QDesktopWidget().screenGeometry()
        myWindow = self.geometry()
        xLocation = (desktop.width() - myWindow.width()) / 2
        yLocation = (desktop.height() - myWindow.height()) / 2
        self.move(xLocation, yLocation)

        #
        # Misc window settings that you can use.
        #
        self.setWindowTitle("Inventory")
        self.setWindowIcon(QtGui.QIcon('./icons/book.png'))
        self.statusBar().showMessage('Inventory')
        self.show()
