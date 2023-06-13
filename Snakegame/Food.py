import turtle as t
import random
from Snake import color_rand
class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.move()

    def move(self):
        self.color(color_rand())
        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(randx, randy)