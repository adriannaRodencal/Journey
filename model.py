import random
import copy
import view
import toolbox

class Model(object):

    def __init__(self):
        self.__frames = []
        self.read_frames('frames.csv')
        self.__currentFrame = self.__frames[0]

    def get_currentFrame(self):
        return self.__currentFrame

    def get_frames(self):
        listOfFrames = []
        for frame in self.__frames:
            listOfFrames.append(frame)
        return listOfFrames

    def read_frames(self, filename):
        """
        Reads in the frames from a file
        :param filename: the name of the file holding the frame information
        :return: None
        """
        #
        # todo! Check to see that the files actually exist in graphics
        #
        with open(filename, 'r') as framesFile:
            for line in framesFile:
                #
                # This is so that the program ignores the comments in the file
                #
                if line[0] != '#':
                    name, button1, button1x, button1y, button2, button2x, button2y, button1Next, button2Next = line.split(
                        ',')
                    name = name.strip()

                    button1 = button1.strip()
                    button1x = button1x.strip()
                    button1y = button1y.strip()
                    if not toolbox.is_number(button1x):
                        raise ValueError(f'{name}: button 1 x coordinate must be a number. Check {filename}.')
                    if not toolbox.is_number(button1y):
                        raise ValueError(f'{name}: button 1 y coordinate must be a number. Check {filename}.')

                    button2 = button2.strip()
                    button2x = button2x.strip()
                    button2y = button2y.strip()
                    if not toolbox.is_number(button2x) and button2x != 'None':
                        raise ValueError(f'{name}: button 2 x coordinate must be a number. Check {filename}.')
                    if not toolbox.is_number(button2y) and button2y != 'None':
                        raise ValueError(f'{name}: button 2 y coordinate must be a number. Check {filename}.')

                    if button2x == 'None':
                        button2x = None
                    if button2y == 'None':
                        button2y = None

                    button1Next = button1Next.strip()
                    button2Next = button2Next.strip()

                    if button2x == None:
                        frame = Frame(self, name, button1, float(button1x), float(button1y), button1Next, button2, button2x,
                                  button2y, button2Next)
                    else:
                        frame = Frame(self, name, button1, float(button1x), float(button1y), button1Next, button2, float(button2x),
                                  float(button2y), button2Next)
                    self.__frames.append(frame)
        print(self.__frames)

    def next_scene(self, theScene, newScene):
        """
        Send view the information needed for making a new scene
        :param theScene: this is from the scene class that view is running
        :param newScene: this is the name of the new scenes photo
        :return: None
        """
        #
        # This seems weird, but it appears to work
        #
        theScene.next_scene(newScene)

class Frame(object):

    def __init__(self, theModel, frameName, button1, button1x, button1y, button1Next, button2, button2x, button2y, button2Next):
        self.__frame = str(frameName)
        self.__theModel = theModel
        self.__button1 = button1
        self.__button1x = button1x
        self.__button1y = button1y
        self.__button1Next = button1Next
        self.__button2 = button2
        self.__button2x = button2x
        self.__button2y = button2y
        self.__button2Next = button2Next

    def find_frame_object(self, list, frameName):
        """
        Given a frames name, this finds the frame object
        :param list: the list the program is looking to find the frame in
        :param frameName: the name of the frame the program is trying to find
        :return: an integer corresponding to the place item is
        """
        location = None
        itemNumber = 0
        while itemNumber < len(list):
            woo = list[itemNumber].get_frame()
            if woo == frameName:
                location = itemNumber
            itemNumber += 1
        frameObject = list[location]
        return frameObject

    def get_frame(self):
        return self.__frame

    def get_button1Next(self):
        """
        Finds the actual frame object that button1Next refers too
        return: an object
        """
        nextFrame = self.find_frame_object(self.__theModel.get_frames(), self.__button1Next)
        return nextFrame

    def get_button2Next(self):
        """
        Finds the actual frame object that button2Next refers too
        return: an object
        """
        nextFrame = self.find_frame_object(self.__theModel.get_frames(), self.__button2Next)
        return nextFrame