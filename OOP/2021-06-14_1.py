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

    def move(self):
        print("move")

    def quack(self):
        print("quack")

    #display method is abstractmethod
    # from abc import abstractmethod
    # 추상method는 실체가 없는 상태 > 메모리에 할당되지 않은 상태,
    # 메모리에 display method가 주소지가 없기 때문에 instance생성 불가
    @abstractmethod
    def display(self):
        pass


class MallardDuck(Duck):

    __myShape = None

    def __init__(self):
        super(MallardDuck, self).__init__()
        self.__myShape = "MallardDuck"
    
    # def __init__(self,x,y):
    #     super(MallardDuck, self).__init__(x,y)
    #     self.__myShape = "MallardDuck"

    # inherit a Duck class for instance
    def display(self):
        print("x : ", self.x,"  y: ",self.y," shape:",self.__myShape)


class RedDuck(Duck):
    __myShape = None

    def __init__(self):
        super(RedDuck, self).__init__()
        self.__myShape = "RedDuck"

    # def __init__(self, x, y):
    #     super(RedDuck, self).__init__(x, y)
    #     self.__myShape = "RedDuck"

    # inherit a Duck class for instance
    def display(self):
        print("x : ", self.x, "  y: ", self.y, " shape:", self.__myShape)



class DuckManager:
    pass

# ------------- Main Test Code ------------- #
md = MallardDuck()
print('use the getter setter')
#use setter
md.x = 20
md.y = 20
print('call getter',md.x, md.y)
md.display()