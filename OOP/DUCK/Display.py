class Display:
    def display(self,SIZE):
        print("x : ", self.x,"  y: ",self.y," shape:",self.__myShape)
        self._turtle.penup()
        self._turtle.goto(self.x, self.y)
        self._turtle.pendown()
        self._turtle.color(self.color)
        self._turtle.begin_fill()
        self._turtle.circle(SIZE)
        self._turtle.end_fill()