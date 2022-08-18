x=100; y=100

class Info:
    #instance 변수
    global x, y
    def __init__(self,x,y,name):
        self.name = name
        self.x = x
        self.y = y
    def info(self, name):
        print("Player Name : ", name)
        #print(" X :",self.x,"  Y: ",self.y)


class Move:

    def up(self,yy):
        global x, y
        y = y - yy
        info = Info
        info.info(self)
        print(y)
    def down(self,yy):
        global x, y
        y = y + yy
        info = Info
        info.info(self)
    def left(self,xx):
        global x, y
        x = x - xx
        info = Info
        info.info(self)
    def right(self,xx):
        global x, y
        x = x + xx
        info = Info
        info.info(self)


class GameObject:
    Info.info()
    Move.up(y)


class Player(GameObject):
    pass


class Enemy(GameObject):
    pass