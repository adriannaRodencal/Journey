import model
import sys, random
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from model import Frame

class Scene(QtWidgets.QWidget):

    def __init__(self, parent=None):

        super(Scene, self).__init__(parent)
        self._button1 = None
        self._button2 = None
        #
        # I'm not sure that this should be created here, but I didn't know where else to put it
        #
        self.theModel = model.Model()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        self._frame = self.theModel.get_currentFrame()

        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.create_buttons()

    def paintEvent(self, event):
        """
        This sets up the background image and text for the scene
        :param event: a value needed for PyQt5 to know
        :return: None
        """
        painter = QtGui.QPainter(self)
        rectangle = self.contentsRect()

        self.background = QtGui.QPixmap()
        root = QtCore.QFileInfo(__file__).absolutePath()
        self.background.load(root + f'/grahics/{self._frame.get_frame()}.jpg')
        #self.create_buttons()

        painter.drawPixmap(rectangle, self.background, rectangle)
        painter.drawText(100, 100, "Hello")

    def keyPressEvent(self, event):
        """
        You could, of course, do more interesting things than print here.
        :param event: a value needed for PyQt5 to know
        :return: None
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
        """
        Sets up the buttons
        :return: None
        """

        self._button1 = QPushButton(self._frame.get_button1(), self)
        self._button1.setToolTip('This is an example button')
        self._button1.move(self._frame.get_button1x(), self._frame.get_button1y())
        self._button1.clicked.connect(self.on_click1)

        if self._frame.get_button2x() != None:
            self._button2 = QPushButton(self._frame.get_button2(), self)
            self._button2.setToolTip('This is an example button')
            self._button2.move(self._frame.get_button2x(), self._frame.get_button2y())
            self._button2.clicked.connect(self.on_click2)

    def on_click1(self):
        """
        Tells the program what scene to show after the user presses button1
        :return: None
        """
        #
        # I don't know if the code should look like this, but it appears to work
        #
        success = self.theModel.determineFail()
        if success == False:
            self.theModel.next_scene(self, self._frame.get_button2Next())
        else:
            self.theModel.next_scene(self, self._frame.get_button1Next())
        print('PyQt5 button click 1')

    def on_click2(self):
        """
        Tells the program what scene to show after the user presses button2
        :return: None
        """
        #
        # I don't know if the code should look like this, but it appears to work
        #
        success = self.theModel.determineFail()
        if success == False:
            self.theModel.next_scene(self, self._frame.get_button2Next())
        else:
            self.theModel.next_scene(self, self._frame.get_button2Next())
        print('PyQt5 button click 1')

    def update_buttons(self):
        """
        Updates the scenes buttons
        :return: None
        """
        self._button1.setText(self._frame.get_button1())
        self._button2.setText(self._frame.get_button2())

    def next_scene(self, newFrame):
        """
        Sets up the next scene
        :return: None
        """
        self._frame = newFrame
        self.update_buttons()
        print('Next Scene')