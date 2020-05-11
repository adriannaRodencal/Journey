import random
import copy
import view
import toolbox
import random
import csv

class Model(object):

    def __init__(self):
        self._frames = []
        self.read_frames('frames.csv')
        self.__currentFrame = self._frames[0]
        self.get_currentFrame()


    def get_currentFrame(self):
        print(self.__currentFrame)
        return self.__currentFrame

    def get_frames(self):
        listOfFrames = []
        for frame in self._frames:
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
                    if len(line.split(',')) != 19:
                        print(line)
                    name, button1, button1x, button1y, button2, button2x, button2y, button1Next, button2Next, success = line.split(
                        ',')
                    name = name.strip()
                    success = success.strip()

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
                                  button2y, button2Next, float(success), location=None)
                    else:
                        frame = Frame(self, name, button1, float(button1x), float(button1y), button1Next, button2, float(button2x),
                                  float(button2y), button2Next, float(success), location=None)


                    self._frames.append(frame)
        print(self._frames)

    def next_scene(self, theScene, newScene):
        """
        Send view the information needed for making a new scene
        :param theScene: this is from the scene class that view is running
        :param newScene: this is the new scenes
        :return: None
        """
        #
        # This seems weird, but it appears to work
        #
        self.__currentFrame = newScene
        theScene.next_scene(newScene)

    def determineFail(self):
        """
        return a boolean of whether an action fails or succeeds
        :param: none
        :return: boolean
        """
        #
        # Taken from our gameOfLife simulation
        #
        if random.randrange(1, 100) > self.__currentFrame.get_success():
            return False
        else:
            return True

    def set_new_scene(self, nextScene):
        """
        Set up the new scene in the Frame class so variables can be pulled out.
        :param nextFrame
        :return: None
        """
        with open('frames.csv', 'r') as framesFile:
            for line in framesFile:
                #
                # This is so that the program ignores the comments in the file
                #
                name, button1, button1x, button1y, button2, button2x, button2y, button1Next, button2Next, success = line.split(
                    ',')
                here = len(name)
                if line[0:here] == nextScene:
                    name = name.strip()
                    success = success.strip()

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

                        frame = Frame(self, name, button1, float(button1x), float(button1y), button1Next, button2,
                                      button2x, button2y, button2Next, success, location=None)
                    else:
                        frame = Frame(self, name, button1, float(button1x), float(button1y), button1Next, button2,
                                      float(button2x), float(button2y), button2Next, success, location=None)
                    print(frame)

class Frame(object):
  
    def __init__(self, theModel, frameName, button1, button1x, button1y, button1Next, button2, button2x, button2y, button2Next, success, location):
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
        self.__success = success
        self.__location = location

    def __str__(self):
        string = f'{self.__frame}, '
        string += f'{self.__button1}, {self.__button1x}, {self.__button1y}, {self.__button1Next}, '
        string += f'{self.__button2}, {self.__button2x}, {self.__button2y}, {self.__button2Next}, '
        string += f'{self.__success}'
        return string

    def get_location(self):
        return self.__location

    def get_success(self):
        return self.__success

    def get_frameName(self):
        return self.__frame

    def get_button1(self):
        return self.__button1

    def get_button1x(self):
        return self.__button1x

    def get_button1y(self):
        return self.__button1y

    def get_button1Next(self):
        return self.__button1Next

    def get_button2(self):
        return self.__button2

    def get_button2x(self):
        return self.__button2x

    def get_button2y(self):
        return self.__button2y

    def get_button2Next(self):
        return self.__button2Next

    def set_location(self, location):
        self.__location = location

    def determineFail(self):
        """
        return a boolean of whether an action fails or succeds
        :param none
        :return: boolean
        """
        #
        # Taken from our gameOfLife simulation
        #
        if random.randrange(1, 100) > Frame.get_success(self):
            return False
        else:
            return True

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
            if list[itemNumber].get_frame() == frameName:
                location = itemNumber
            itemNumber += 1
        frameObject = list[location]
        self.set_location(location)
        return frameObject

    def get_frame(self):
        return self.__frame

    def get_button1Next(self):
        """
        Finds the actual frame object that button1Next refers too
        return: an object
        """
        nextFrame = self.find_frame_object(self.__theModel.get_frames(), self.__button1Next)
        self.__theModel.set_new_scene(self.__button1Next)
        return nextFrame

    def get_button2Next(self):
        """
        Finds the actual frame object that button2Next refers too
        return: an object
        """
        nextFrame = self.find_frame_object(self.__theModel.get_frames(), self.__button2Next)
        self.__theModel.set_new_scene(self.__button2Next)
        return nextFrame


