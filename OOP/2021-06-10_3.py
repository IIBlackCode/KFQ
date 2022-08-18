import random
import turtle

# Super Class
class Duck:

    # instance value
    def __init__(self):
        #         self.__color = ''
        self.x = random.randint(-400, 400)
        self.y = random.randint(-400, 400)
        self.size = 30
        self.__turtle = None

    def display(self, turtle):
        print(self.x, ',', self.y, '=', self.size)
        self.__turtle = turtle
        self.__turtle.penup()
        self.__turtle.shape("turtle")
        self.__turtle.color("#FFAA55")
        self.__turtle.begin_fill()
        self.__turtle.circle(self.size)
        self.__turtle.end_fill()
        self.__turtle.setposition(self.x,self.y)


    def screen_reset(self):
        self.__turtle.reset()

#Duck 객체 10마리 만들기
duck_list = []
for i in range(0,10):
    duck_list.append(Duck())

for v in duck_list:
    v.display(turtle)