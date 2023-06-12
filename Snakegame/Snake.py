import turtle as t
import random
MOVE = 20 #constants go to top of module
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

def color_rand():
    first = random.randint(0, 255)
    second = random.randint(0, 255)
    third = random.randint(0, 255)
    return(first, second, third)
class Snake:
    def __init__(self):
        self.coordinates = [(0, 0), (20, 0), (40, 0)]
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]


    def make_snake(self):
        for place in self.coordinates:
            seg = t.Turtle("square")
            seg.penup()
            t.colormode(255)
            seg.color(color_rand())
            seg.goto(place)
            self.segments.append(seg)
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            xnew = self.segments[seg - 1].xcor()  # assigns the prior segments coord to current moving segment
            ynew = self.segments[seg - 1].ycor()
            self.segments[seg].goto(xnew, ynew)
            #screen.update()
            #time.sleep(1)
        self.segments[0].forward(MOVE)

    def new_seg(self):
        last = len(self.segments) - 1
        lastx = self.segments[last].xcor()
        lasty = self.segments[last].ycor()
        newseg = t.Turtle("square")
        newseg.penup()
        t.colormode(255)
        newseg.color(color_rand())
        newseg.goto(lastx+20, lasty)
        self.segments.append(newseg)


    def down(self):
        #self.segments[0].setheading(270)
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        self.head.color(color_rand())


    def up(self):
        if self.head.heading() != DOWN: #check for direction reverse (not allowed)
            self.head.setheading(UP)
        self.head.color(color_rand())
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        self.head.color(color_rand())
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        self.head.color(color_rand())


