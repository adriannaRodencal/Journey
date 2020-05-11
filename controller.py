import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from time import sleep
from view import Scene


class MyApplication(QtWidgets.QMainWindow):
    def __init__(self, app):
        #
        # Call __init__ for the parent class to initialize things.
        #
        super(MyApplication, self).__init__()

        #
        # Keep a reference to the app so we can explicitly call self.app.processEvents().
        #
        self.app = app

        #
        # Setup the main display window.
        #
        self.setup_window()

        #
        # Initialize the widget that will act as the display.
        #
        self.display = Scene()
        self.setCentralWidget(self.display)
        self.display.show()

        #
        # Create actions, menus, toolbars and statusbar
        #
        self.create_actions()
        self.create_menus()
        self.create_tool_bars()
        self.create_status_bar()

    def setup_window(self):
        """
        Just putting a bunch of loosely related window setup stuff together here. This could
        have gone in __init__(), but it was getting long.
        """
        #
        # Starting size of window. I don't think this is required.
        #
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
        self.setWindowTitle("Treekthin ota ta Churi")
        self.setWindowIcon(QtGui.QIcon('./icons/book.png'))
        self.statusBar().showMessage('Opening')
        self.show()

    def create_actions(self):
        """
        Setup an action that can be associated with menus, buttons, shortcuts and taskbars.
        Anything action that is initiated by interacting with the user interface (as opposed
        to clicking directly in a window is setup here.
        """
        #
        # Root is where the application exists in the directory structure.
        #
        root = QtCore.QFileInfo(__file__).absolutePath()

        self.exitAction = QtWidgets.QAction("E&xit", self,
                                            shortcut="Ctrl+Q",
                                            statusTip="Exit the application",
                                            triggered=self.quit)

        self.aboutAction = QtWidgets.QAction("&About", self,
                                             statusTip="More information about the program",
                                             triggered=self.about)

        self.inventoryAction = QtWidgets.QAction("&Inventory", self,
                                            statusTip="Show Inventory",
                                            triggered=self.inventory)

    def create_menus(self):
        """Create a menubar and add a menu and an action."""

        self.addAction(self.exitAction)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.inventoryAction)
        self.helpMenu.addAction(self.aboutAction)

    def create_tool_bars(self):
        """Create a toolbar and add an action to it."""

        #self.fileToolBar = self.addToolBar("File")
        #self.fileToolBar.addAction(self.newAction)
        #self.fileToolBar.addAction(self.openAction)
        #self.fileToolBar.addAction(self.saveAction)


    def create_status_bar(self):
        self.statusBar().showMessage("Opening")
        #
        # You can also add widgets to the statusBar
        #
        # self.progressBar = QtWidgets.QProgressBar(self.statusBar())
        # self.progressBar.hide()
        # self.statusBar().addPermanentWidget(self.progressBar)

    def quit(self):
        self.close()

    def about(self):
        QtWidgets.QMessageBox.about(self, "Treekthin ota at Churi",
                                    "On this journey you need to find your friend "
                                    "who went missing while traveling in the "
                                    "mountains. Choose your path carefully because "
                                    "one small error could ruin everything.")

    def inventory(self):
        QtWidgets.QMessageBox.about(self, "Treekthin ota at Churi",
                                    "Inventory")

    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        print(x, y)
        currentFrame = self.display.get_frame()
        if currentFrame.get_frameName() == 'emptyCave':
            if 764 < x < 835 and 337 < y < 392:
                self.display.theModel.next_scene(self.display, currentFrame.get_button2Next())
