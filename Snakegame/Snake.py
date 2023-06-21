import turtle as t
import random
MOVE = 20 #constants go to top of module
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

def color_rand():
    first = random.randint(1, 255) #avoid 000=bgcolor
    second = random.randint(1, 255)
    third = random.randint(1, 255)
    return(first, second, third)
class Snake:
    def __init__(self):
        self.coordinates = [(0, 0), (20, 0), (40, 0)]
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]


    def make_snake(self):
        for place in self.coordinates:
            self.new_seg(place)

    def new_seg(self, pos):
        newseg = t.Turtle("square")
        newseg.penup()
        t.colormode(255)
        newseg.color(color_rand())
        newseg.goto(pos)
        self.segments.append(newseg)

    def move(self):
        for segn in range(len(self.segments) - 1, 0, -1):
            xnew = self.segments[segn - 1].xcor()  # assigns the prior segments coord to current moving segment
            ynew = self.segments[segn - 1].ycor()
            self.segments[segn].goto(xnew, ynew)
            #screen.update()
            #time.sleep(1)
        self.head.forward(MOVE)

    def add_seg(self):
        #last = self.segments[-1] #-1 in python holds last list element
        #newx = self.segments[last].xcor()+20
        #lasty = self.segments[last].ycor()
        self.new_seg(self.segments[-1].position())


    def down(self):

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

    def new_game(self):
        self.clear()
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]



