from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.goto(0,0)

        #self.move()

    def move(self):
        self.goto(self.xcor()+self.xmove, self.ycor()+self.ymove)

    def y_bounce(self):
        self.ymove = -1 * self.ymove
        '''if self.heading() ==0:
            self.setheading(180)
        elif self.heading() ==180:
            self.setheading(0)
        elif self.heading() ==90:
            self.setheading(270)
        elif self.heading()==270:
            self.setheading(90)'''
    def x_bounce(self):
        self.xmove = -1 * self.xmove
        #self.move()
        #self.goto(self.xcor() - 20, self.ycor() - 20)

    def reset(self):
        self.goto(0,0)
        self.x_bounce()


