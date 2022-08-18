import random
import turtle
from abc import *


class Duck:
    def __init__(self):
        self._x = random.randint(-300, 300)
        self._y = random.randint(-300, 300)
        self._size = 30
        self._turtle = turtle

    @abstractmethod
    def display(self):
        pass


class Fly:
    _turtle = turtle

    def fly(self):
        self._turtle.penup()
        self._turtle.goto(self._x - 50, self._y - 10)
        self._turtle.pendown()
        self._turtle.color('black')
        self._turtle.write("날다")


class Swim:
    _turtle = turtle

    def swim(self):
        self._turtle.penup()
        self._turtle.goto(self._x - 50, self._y + 50)
        self._turtle.pendown()
        self._turtle.color('black')
        self._turtle.write("수영")


class Quack:
    @abstractmethod
    def quack(self):
        pass


class RedDuck(Duck, Fly, Swim, Quack):
    def __init__(self):
        super(RedDuck, self).__init__()

    def display(self):
        self._turtle.penup()
        self._turtle.goto(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color('red')
        self._turtle.begin_fill()
        self._turtle.circle(self._size)
        self._turtle.end_fill()
        self.quack()
        self.fly()
        self.swim()

    def quack(self):
        self._turtle.penup()
        self._turtle.goto(self._x + 30, self._y + 50)
        self._turtle.pendown()
        self._turtle.color('black')
        self._turtle.write("꽥꽥")


class MallardDuck(Duck, Fly, Swim, Quack):
    def __init__(self):
        super(MallardDuck, self).__init__()

    def display(self):
        self._turtle.penup()
        self._turtle.goto(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color('blue')
        self._turtle.begin_fill()
        self._turtle.circle(self._size)
        self._turtle.end_fill()
        self.quack()
        self.fly()
        self.swim()

    def quack(self):
        self._turtle.penup()
        self._turtle.goto(self._x + 30, self._y + 50)
        self._turtle.pendown()
        self._turtle.color('black')
        self._turtle.write("꽥꽥")


class RubberDuck(Duck, Swim, Quack):
    def __init__(self):
        super(RubberDuck, self).__init__()

    def display(self):
        self._turtle.penup()
        self._turtle.goto(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color('blue')
        self._turtle.begin_fill()
        self._turtle.circle(self._size)
        self._turtle.end_fill()
        self.quack()
        self.swim()

    def quack(self):
        self._turtle.penup()
        self._turtle.goto(self._x + 30, self._y + 50)
        self._turtle.pendown()
        self._turtle.color('red')
        self._turtle.write("삑삑")


class DecoyDuck(Duck, Swim):
    def __init__(self):
        super(DecoyDuck, self).__init__()

    def display(self):
        self._turtle.penup()
        self._turtle.goto(self._x, self._y)
        self._turtle.pendown()
        self._turtle.color('blue')
        self._turtle.begin_fill()
        self._turtle.circle(self._size)
        self._turtle.end_fill()
        self.swim()


class DuckManager:
    __duck_list = []

    def __init__(self):
        self.makeDucks()

    def makeDucks(self):
        __duck_kind = [MallardDuck(), RedDuck(), RubberDuck(), DecoyDuck()]
        for duck in range(10):
            DuckManager.__duck_list.append(__duck_kind[random.randint(0, 3)])

    def dispDucks(self):
                for duck in DuckManager.__duck_list:
                    if duck != None:
                        duck.display()



DM = DuckManager()
DM.dispDucks()