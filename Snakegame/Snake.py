import turtle as t
MOVE = 20 #constants go to top of module
class Snake:
    def __init__(self):
        self.coordinates = [(0, 0), (20, 0), (40, 0)]
        self.segments = []
        self.make_snake()


    def make_snake(self):
        for place in self.coordinates:
            seg = t.Turtle("square")
            seg.penup()
            seg.color("white")
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
