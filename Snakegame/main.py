import time
import turtle as t
import Snake as s

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turns automatic animation off

segments = []
game_on = True
snake = s.Snake()

# def multi_square(numsquare):
#     count = 0
#     xcoord = 0
#     while count < numsquare:
#         sq = t.Turtle(shape="square")
#         sq.color("white")
#         sq.penup()
#
#         if count == 0:
#             sq.goto(0, 0)
#             print(xcoord)
#         else:
#             sq.goto(xcoord, 0)
#             print(xcoord)
#
#         segments.append(sq)
#         count += 1
#         xcoord += 20

coordinates = [(0,0), (20,0), (40,0)]
def make_segs(coord):
    for place in coord:
        seg = t.Turtle("square")
        seg.penup()
        seg.color("white")
        seg.goto(place)
        segments.append(seg)



while game_on:
    screen.update() #refresh screen
    time.sleep(0.1)
    snake.move()



screen.exitonclick()
