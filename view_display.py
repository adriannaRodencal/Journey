import sys, random
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

class MainWidget(QtWidgets.QWidget):

    def __init__(self, controller, parent=None):
        super(MainWidget, self).__init__(parent)

        #
        # Pass in the controller because we'll need some information from it
        # in order to draw whatever non-trivial thing we want to eventual draw
        # in stead of those lines. In the past I've passed in the
        # whole app, but I don't think I need all that (could be wrong).
        #
        self.controller = controller

        #
        # If you are going to use a timer, create one. Oh, and look up timers.
        #
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        #
        # I'm not actually sure why I thought this was a good idea.
        # Someone should really look into this.
        #
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        #
        # You can set a background if you'd like:
        #
        self.background = QtGui.QPixmap()
        root = QtCore.QFileInfo(__file__).absolutePath()
        self.background.load(root + '/graphics/riverChose.jpg')

        #
        # You can have a painter draw directly onto this widget, but you have more
        # options when you draw on an image. We will do that a little later.
        #
        # self.image = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        # self.image.fill(10)


        #
        # This is an example of connecting a widget (slider) to an instance variable. It is
        # only for drawing the lines in this example. You won't need it.
        #
        self.lines = 25


    def paintEvent(self, event):
        """
        By magic, this event occasionally gets called. Maybe on self.update()? Certainly on
        a window resize.
        """
        painter = QtGui.QPainter(self)
        rectangle = self.contentsRect()

        #
        # Set Background
        #
        painter.drawPixmap(rectangle, self.background, rectangle)

        #
        # If we were drawing on an image, we would need to do some resizing
        # stuff like this. We will do this eventually.
        #
        newSize = self.size()
        self.image = self.image.scaled(newSize)
        painter.drawImage(0, 0, self.image)

        #
        # Do any drawing that you need to do next.
        #
        self.draw_random_lines(painter)

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

    def draw_random_lines(self, painter):
        width = self.width()
        height = self.height()
        for x in range(self.lines):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)

            #
            # Just your normal HTML color codes. Look them up.
            #
            # red = random.choice(['ff', 'dd', '99', '66', '33', '00'])
            # print(red)
            # green = random.choice(['ff', 'dd', '99', '66', '33', '00'])
            # blue = random.choice(['ff', 'dd', '99', '66', '33', '00'])
            red = random.choice(['ff', 'dd', '99', '66'])
            green = random.choice(['ff', 'dd', '99'])
            blue = random.choice(['ff', 'dd', '99', '66', '33', '00'])
            color = QtGui.QColor('#' + red + green + blue)
            penWidth = random.randint(1,15)
            pen = QtGui.QPen(color, penWidth)
            painter.setPen(pen)
            painter.drawLine(x1, y1, x2, y2)
            painter.drawEllipse(x1/2, y1/2, x2/2, y2/2)
            painter.drawRect(x1/3, y1/3, x2/3, y2/3)

    def set_lines(self, lines):
        self.lines = lines
        self.update()

    def mousePressEvent(self, event):
        print("click (display)")

    def mouseReleaseEvent(self, event):
        print("release (display)")

    def draw_roaming_lines(self, painter):
        self.roamer.advance()
        red = 'ff'
        blue = 'ff'
        green = 'ff'
        color = QtGui.QColor('#' + red + green + blue)
        penWidth = 2
        pen = QtGui.QPen(color, penWidth)
        painter.setPen(pen)
        painter.drawLine(line.start.x, line.start.y, line.end.x, line.end.y)

