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
                    print("[ ", i, ",", j, " ]", end=" ")
                    # print("\t\t",end=" ")
            print("")

duck = Duck(5,5)
duck.color = "빨간"
duck.output()
duck.location()

duck = Duck(4,2)
duck.color = "노란"
duck.output()
duck.location()

duck = Duck(2,9)
duck.color = "청동"
duck.output()
duck.location()

class DuckManager:
    def __init__(self):
        self.__list = []

    def display(self):
        self.__list.pop()
