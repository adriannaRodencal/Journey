import model
import sys, random
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Scene(QtWidgets.QWidget):

    def __init__(self, parent=None, frame='mountainChoice', possiblePaths=2):

        super(Scene, self).__init__(parent)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        self.frame = frame

        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.create_buttons()


    def paintEvent(self, event):
        """
        By magic, this event occasionally gets called. Maybe on self.update()? Certainly on
        a window resize.
        """
        painter = QtGui.QPainter(self)
        rectangle = self.contentsRect()

        self.background = QtGui.QPixmap()
        root = QtCore.QFileInfo(__file__).absolutePath()
        self.background.load(root + f'/grahics/{self.frame}.jpg')
        
        painter.drawPixmap(rectangle, self.background, rectangle)
        painter.drawText(100, 100, "Hello")


    def keyPressEvent(self, event):
        """
        You could, of course, do more interesting things than print here.
        :param event:
        :return:
        """
        if event.key() in [QtCore.Qt.Key_Right, QtCore.Qt.Key_Up]:
            print('up')
        elif event.key() in [QtCore.Qt.Key_Left, QtCore.Qt.Key_Down]:
            print('down')
        elif event.key() in [QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return, QtCore.Qt.Key_Space]:
            print('select')
            self.update()

    def wheelEvent(self, event):
        """should work a lot like keypress..."""
        if event.angleDelta().y() > 0:
            print('up')
        else:
            print('down')

    def create_buttons(self):
        button1 = QPushButton('PyQt5 button', self)
        button1.setToolTip('This is an example button')
        button1.move(250, 625)
        button1.clicked.connect(self.on_click)
        
        button2 = QPushButton('This is random', self)
        button2.setToolTip('This is an example button')
        button2.move(1025, 550)
        button2.clicked.connect(self.on_click)

    def on_click(self):
        print('PyQt5 button click')