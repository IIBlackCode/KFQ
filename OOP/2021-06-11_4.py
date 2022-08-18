import random
import turtle
from abc import *

class Duck(metaclass=ABCMeta):

    SIZE = 30
    count = 0

    def __init__(self):
        self._x = random.randint(-300,300)
        self._y = random.randint(-300,300)
        self._turtle = turtle
        Duck.count += 1

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

    # duck count
    def countMethod(self):
        self._turtle.color("#000000")
        self._turtle.penup()
        self._turtle.goto(self._x - 30, self._y - 30)
        self._turtle.pendown()
        write = str(Duck.count)
        self._turtle.write(write)
        print(write)

    def output(self):
        self.display()
        self.sound()
        self.move()
        self.countMethod()

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
    # def __init__(self):

    def displayAllDucks(self):
        for i in range(0,10):
            randomv = random.randint(0, 1)
            print("랜덤",randomv)
            if randomv == 1:
                self.duckList.append(MallardDuck())
                self.duckList[i].output()
            else:
                self.duckList.append(RedDuck())
                self.duckList[i].output()



dm = DuckManager()
dm.displayAllDucks()

# PYTHON_PRACTICE = DuckManager('#FF00FF')
# PYTHON_PRACTICE.displayAllDucks()