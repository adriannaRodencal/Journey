import random
import copy
import view

class Model(object):

    def __init__(self):
        self.__currentScene = None

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
