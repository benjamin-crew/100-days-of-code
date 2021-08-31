from turtle import Turtle

class StateClass(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.draw_to_screen()

    def draw_to_screen(self):
        self.setposition(self.x, self.y)
        self.write(f"{self.name}", align="center", font=("Arial", 10, "normal"))