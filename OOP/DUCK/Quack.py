class Quack:
    def quack(self, message):
        print("quack")
        self._turtle.color("#FFAA00")
        self._turtle.penup()
        self._turtle.goto(self.x + 30, self.y + 50)
        self._turtle.pendown()
        self._turtle.write(message)