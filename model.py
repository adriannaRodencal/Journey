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