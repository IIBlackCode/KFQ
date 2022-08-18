class Fly:
    def fly(self):
        self._turtle.color("#000000")
        self._turtle.penup()
        self._turtle.goto(self.__x - 30, self.__y - 30)
        self._turtle.pendown()
        self._turtle.write("날다")