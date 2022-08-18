import random
import turtle
from abc import *

class Duck(metaclass=ABCMeta):

    SIZE = 30

    def __init__(self):
        self._x = random.randint(-300,300)
        self._y = random.randint(-300,300)
        self._turtle = turtle

    #추상클래스
    @abstractmethod
    def display(self):
        # print("X : ", self.x, "  Y : ", self.y)
        pass
    
    #duck sound
    def sound(self):
        self._turtle.color("#FFAA00")
        self._turtle.penup()
        self._turtle.goto(self._x + 30, self._y + 50)
        self._turtle.pendown()
        self._turtle.write("quack")
    
    #duck move
    def move(self):
        self._turtle.color("#FF00AA")
        self._turtle.penup()
        self._turtle.goto(self._x - 55, self._y + 50)
        self._turtle.pendown()
        self._turtle.write("move")

    # duck move
    def count(self):
        # self._turtle.color("#FFFFFF")
        # self._turtle.penup()
        # self._turtle.goto(self._x - 55, self._y + 30)
        # self._turtle.pendown()
        write = str(Duck.count)
        print(write)
        # self._turtle.write(write)

    def output(self):
        self.display()
        self.sound()
        self.move()
        self.count()

class MallardDuck(Duck):
    color = ''

    def __init__(self):
        super(MallardDuck, self).__init__()
        self.color = '#0000FF'

    #추상클래스 재정의
    def display(self):
        self._turtle.penup()
        self._turtle.goto(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color(self.color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.SIZE)
        self._turtle.end_fill()


class RedDuck(Duck):
    color = ''

    def __init__(self):
        super(RedDuck, self).__init__()
        self.color = '#FF0000'

    # 추상클래스 재정의
    def display(self):
        self._turtle.penup()
        self._turtle.goto(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color(self.color)
        self._turtle.begin_fill()
        self._turtle.circle(Duck.SIZE)
        self._turtle.end_fill()


class DuckManager:
    duckList = []
    def __init__(self):
        for i in range(0,5):
            self.duckList.append(MallardDuck())
            self.duckList.append(RedDuck())

    def displayAllDucks(self):
        for duck in self.duckList:
            duck.output()
            print(duck)


dm = DuckManager()
dm.displayAllDucks()

# PYTHON_PRACTICE = DuckManager('#FF00FF')
# PYTHON_PRACTICE.displayAllDucks()