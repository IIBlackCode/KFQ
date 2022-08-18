import random
import turtle
from abc import abstractmethod
from abc import ABCMeta
from abc import *

class Duck(metaclass=ABCMeta):
    x = None
    y = None

    def __init__(self):
        self.__x = random.randint(-300, 300)
        self.__y = random.randint(-300, 300)

    #The impossible Constructor Overloading
    # def __init__(self,x,y):
    #     self.__x = x
    #     self.__y = y

    # decorator pattern
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, x):
        self.__y = x