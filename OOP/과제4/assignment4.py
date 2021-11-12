# [과제4][본인이름] 슈팅게임 속 적기객체와 플레이어 객체의 역할을 정의하고, 클래스다이어그램으로 작성하시오.

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def up(self):
        self.y += 10
        print("Up")
    def down(self):
        self.y -= 10
        print("Down")
    def left(self):
        self.x -= 10
        print("Left")
    def right(self):
        self.x += 10
        print("Right")


class Player:
    def __init__(self):
        self.x = 5
        self.y = 5

    def left(self):
        self.x -= 1
        print("Left")
    def right(self):
        self.x += 1
        print("Right")
