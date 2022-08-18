import random
import turtle
from abc import abstractmethod
from abc import ABCMeta
from abc import *

class Duck(metaclass=ABCMeta):
    x = None
    y = None
    SIZE = 30
    def __init__(self):
        self.__x = random.randint(-300, 300)
        self.__y = random.randint(-300, 300)
        self._turtle = turtle
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

    #display method is abstractmethod
    # from abc import abstractmethod
    # 추상method는 실체가 없는 상태 > 메모리에 할당되지 않은 상태,
    # 메모리에 display method가 주소지가 없기 때문에 instance생성 불가
    @abstractmethod
    def display(self):
        pass

    def swim(self):
        self._turtle.color("#FF00AA")
        self._turtle.penup()
        self._turtle.goto(self.x - 55, self.y + 50)
        self._turtle.pendown()
        self._turtle.write("SWIM")

    # duck move
    def fly(self):
        self._turtle.color("#000000")
        self._turtle.penup()
        self._turtle.goto(self.__x - 30, self.__y - 30)
        self._turtle.pendown()
        # write = str(Duck.count)
        self._turtle.write("날다")


class MallardDuck(Duck):

    __myShape = None
    color = None

    def __init__(self):
        super(MallardDuck, self).__init__()
        self.__myShape = "MallardDuck"
        self.color = '#0000FF'

    # def __init__(self,x,y):
    #     super(MallardDuck, self).__init__(x,y)
    #     self.__myShape = "MallardDuck"

    # inherit a Duck class for instance
    def display(self):
        print("x : ", self.x,"  y: ",self.y," shape:",self.__myShape)
        self._turtle.penup()
        self._turtle.goto(self.x, self.y)
        self._turtle.pendown()
        self._turtle.color(self.color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.SIZE)
        self._turtle.end_fill()

    def quack(self, message):
        print("quack")
        self._turtle.color("#FFAA00")
        self._turtle.penup()
        self._turtle.goto(self.x + 30, self.y + 50)
        self._turtle.pendown()
        self._turtle.write(message)

    def output(self):
        self.display()
        self.swim()
        self.quack("꽥꽥")
        self.fly()

class RedDuck(Duck):
    __myShape = None
    color = None

    def __init__(self):
        super(RedDuck, self).__init__()
        self.__myShape = "RedDuck"
        self.color = '#FF0000'

    # def __init__(self, x, y):
    #     super(RedDuck, self).__init__(x, y)
    #     self.__myShape = "RedDuck"

    # inherit a Duck class for instance
    def display(self):
        print("x :\t", self.x, "\ty:\t", self.y, "\tshape:", self.__myShape)
        self._turtle.penup()
        self._turtle.goto(self.x, self.y)
        self._turtle.pendown()
        self._turtle.color(self.color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.SIZE)
        self._turtle.end_fill()

    def quack(self, message):
        print("quack")
        self._turtle.color("#FFAA00")
        self._turtle.penup()
        self._turtle.goto(self.x + 30, self.y + 50)
        self._turtle.pendown()
        self._turtle.write(message)

    def output(self):
        self.display()
        self.swim()
        self.quack("꽥꽥")
        self.fly()

class RubberDuck(Duck):
    __myShape = None
    color = None

    def __init__(self):
        super(RubberDuck, self).__init__()
        self.__myShape = "RedDuck"
        self.color = '#AAAA00'

    # def __init__(self, x, y):
    #     super(RedDuck, self).__init__(x, y)
    #     self.__myShape = "RedDuck"

    # inherit a Duck class for instance
    def display(self):
        print("x :\t", self.x, "\ty:\t", self.y, "\tshape:", self.__myShape)
        self._turtle.penup()
        self._turtle.goto(self.x, self.y)
        self._turtle.pendown()
        self._turtle.color(self.color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.SIZE)
        self._turtle.end_fill()

    def quack(self, message):
        print("quack")
        self._turtle.color("#FFAA00")
        self._turtle.penup()
        self._turtle.goto(self.x + 30, self.y + 50)
        self._turtle.pendown()
        self._turtle.write(message)

    def output(self):
        self.display()
        self.swim()
        self.quack("삑삑")
        # self.fly()

class DecoyDuck(Duck):
    __myShape = None
    color = None

    def __init__(self):
        super(DecoyDuck, self).__init__()
        self.__myShape = "RedDuck"
        self.color = '#00FF00'

    # def __init__(self, x, y):
    #     super(RedDuck, self).__init__(x, y)
    #     self.__myShape = "RedDuck"

    # inherit a Duck class for instance
    def display(self):
        print("x :\t", self.x, "\ty:\t", self.y, "\tshape:", self.__myShape)
        self._turtle.penup()
        self._turtle.goto(self.x, self.y)
        self._turtle.pendown()
        self._turtle.color(self.color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.SIZE)
        self._turtle.end_fill()

    def output(self):
        self.display()
        self.swim()
        # self.quack("삑삑")
        # self.fly()

#10마리를 랜덤하게 담기
class DuckManager:
    # MallardDuck[] mlist
    # RedDuck[] rlist

    __duck_list = []
    __instance = None

    def __init__(self):
        self.makeDucks()

        #내부에 인스턴스가 있는지 확인
        #   인스턴스가 이미 있다면 이미 있는걸로 사용, 없으면 생성
        if not DuckManager.__instance:
            print("creation")
        else:
            print("already", self.getInstance())

    def makeDucks(self):
        #랜덤하게 20마리
        for i in range(0,20):
            rDuck = random.randint(0,4)
            if rDuck == 0:
                print("RedDuck")
                DuckManager.__duck_list.append(RedDuck())
            elif rDuck == 1:
                print("MallardDuck")
                DuckManager.__duck_list.append(MallardDuck())
            elif rDuck == 2:
                print("RubberDuck")
                DuckManager.__duck_list.append(RubberDuck())
            elif rDuck == 3:
                print("DecoyDuck")
                DuckManager.__duck_list.append(DecoyDuck())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = DuckManager()
        return cls.__instance

    def displayAllDucks(self):
        for duck in DuckManager.__duck_list:
            # duck.display()
            duck.output()
# ------------- Main Test Code ------------- #
dm = DuckManager()
dm.displayAllDucks()
