import random
import copy
import view
import toolbox

class Model(object):

    def __init__(self):
        self.__currentScene = 'mountainChoice'
        self.__frames = []
        self.read_frames('frames.csv')

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
                    if not toolbox.is_number(button2x):
                        raise ValueError(f'{name}: button 2 x coordinate must be a number. Check {filename}.')
                    if not toolbox.is_number(button2y):
                        raise ValueError(f'{name}: button 2 y coordinate must be a number. Check {filename}.')

                    button1Next = button1Next.strip()
                    button2Next = button2Next.strip()

                    frame = Frame(name, button1, float(button1x), float(button1y), button2, float(button2x),
                                  float(button2y), button1Next, button2Next)
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

    def __init__(self, frameName, button1, button1x, button1y, button1Next, button2, button2x, button2y, button2Next):
        self.__frame = frameName
        self.__button1 = button1
        self.__button1x = button1x
        self.__button1y = button1y
        self.__button1Next = button1Next
        self.__button2 = button2
        self.__button2x = button2x
        self.__button2y = button2y
        self.__button2Next = button2Next
