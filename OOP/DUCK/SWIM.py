class Swim:
    def swim(self):
        self._turtle.color("#FF00AA")
        self._turtle.penup()
        self._turtle.goto(self.x - 55, self.y + 50)
        self._turtle.pendown()
        self._turtle.write("SWIM")