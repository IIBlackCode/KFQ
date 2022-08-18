class Duck:
    x = None
    y = None
    SIZE = None

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.SIZE = 30

    def display(self):
        print(self.x)
        print(self.y)
        print(self.SIZE)

    def move(self):
        pass

    def sound(self):
        pass


class MallardDuck(Duck):
    super(3,3)
    def display(self):
        pass


class RedDuck(Duck):
    def display(self):
        pass