import turtle as t
import random

def color_rand():
    first = random.randint(1, 255) #avoid 000=bgcolor
    second = random.randint(1, 255)
    third = random.randint(1, 255)
    return(first, second, third)

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        t.colormode(255)
        self.color(color_rand())
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1
        self.goto(0,0)

        #self.move()

    def move(self):
        self.goto(self.xcor()+self.xmove, self.ycor()+self.ymove)

    def y_bounce(self):
        self.ymove = -1 * self.ymove
        self.move_speed *= 0.9

    def x_bounce(self):
        self.xmove = -1 * self.xmove
        self.move_speed *= 0.9 #ball speed increases w bounce
        #self.goto(self.xcor() - 20, self.ycor() - 20)

    def reset(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.color(color_rand())
        self.x_bounce()


