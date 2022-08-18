from DUCK.Display import Display
from DUCK.Duck import Duck
from DUCK.Fly import Fly
from DUCK.Quack import Quack
from DUCK.SWIM import Swim


class RubberDuck(Duck,Display,Swim,Quack):
    def __init__(self):
        print("MallardDuck")