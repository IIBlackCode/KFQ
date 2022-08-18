class Duck:
    
    # instance value
    def __init__(self,x,y):
        self.__color = ''
        self.__x = x
        self.__y = y


    # decorator pattern
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


    # Method
    def display(self):
        print("[",self.__color, "Duck]")

    def move(self):
        print(self.__color,"Duck : 걷기")

    def sound(self):
        print(self.__color,"Duck : 삑삑")

    def output(self):
        self.display()
        self.move()
        self.sound()

    def location(self):

        for i in range (1,6):
            for j in range (1,11):
                if self.__x == i and self.__y == j :
                    # print("[", i, ",", j, "]", end=" ")
                    print("[",self.__color,"오리 ]", end=" ")
                else:
                    print("||||||||||||",end=" ")
            print("")

redDuck = Duck(5,5)
redDuck.color = "빨간"
redDuck.output()
redDuck.location()

yellowDuck = Duck(4,7)
yellowDuck.color = "노란"
yellowDuck.output()
yellowDuck.location()

yellowDuck = Duck(2,9)
yellowDuck.color = "청동"
yellowDuck.output()
yellowDuck.location()