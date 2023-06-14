from turtle import  Turtle
class Paddle(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.color("white")
        self.shape("square")
        #self.width = 20
        #self.height = 100
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.penup()
        self.goto(direction)

    def down(self):
        #self.setheading(270)
        self.goto(self.xcor(), self.ycor() -20)

    def up(self):
        self.goto(self.xcor(), self.ycor() +20)



