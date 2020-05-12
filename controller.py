import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from time import sleep
from view import Scene
from intentory import Inventory


class MyApplication(QtWidgets.QMainWindow):
    def __init__(self, app):
        # MainWindow is, as you might expect, the main window
        # of an application. It supports menus, status bars,
        # toolbars and probably other stuff.
        #
        # Call __init__ for the parent class to initialize things.
        super(MyApplication, self).__init__()

        #
        # Keep a reference to the app so we can explicitly call self.app.processEvents().
        # You won't have to worry about this for a while. You'll know when you need it.
        #
        self.app = app

        #
        # Setup the main display window.

        self.setup_window()
        #
        # Initialize the widget that will act as the display.
        #
        self.display = Scene()
        self.setCentralWidget(self.display)
        self.display.show()


        #l
        # Create actions, menus, toolbars and statusbar
        #
        self.create_actions()
        self.create_menus()
        self.create_status_bar()

        # self.event = MyLabel()
        # self.event.show()

        #
        # This example only has one item in the main window. If you write
        # a program where you have multiple items in the main window then
        # you can control the layout of those items. Layout here means
        # the relationship between the items on the screen. This can
        # become complicated as users resize things, so "layouts" really
        # help with that.
        #
        # There are: Vertical Box Layouts (QVBoxLayout), Horizontal Box
        # Layouts (QHBoxLayout) and Grid Layouts (QGridLayout).
        #
        # Try it without these lines commented out. It is a subtle difference.
        # See the layouts examples for, well, examples.
        #
        #mainLayout = QtWidgets.QVBoxLayout()
        #mainLayout.addWidget(self.display)
        #self.setLayout(mainLayout)

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
        self.helpMenu.addAction(self.aboutAction)

        self.inventoryMenu = self.menuBar().addMenu("&Inventory")
        self.inventoryMenu.addAction(self.inventoryAction)


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
        self.inventory = Inventory()
        self.inventory.show()
        # QtWidgets.QMessageBox.about(self, "Treekthin ota at Churi",
        #                             "Inventory")

    def mousePresEvent(self, event):
        print("click (display)")
        x = event.pos().x()
        y = event.pos().y()
        print(x, y)
