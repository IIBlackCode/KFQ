from DUCK.Display import Display
from DUCK.Duck import Duck
from DUCK.Fly import Fly
from DUCK.Quack import Quack
from DUCK.SWIM import Swim


class MallardDuck(Duck,Display,Swim,Quack,Fly):
    def __init__(self):
        print("MallardDuck")