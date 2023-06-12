import time
import turtle as t
import Snake as s
from Food import Food
screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turns automatic animation off

segments = []
game_on = True
snake = s.Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

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
    #collision detection
    if snake.head.distance(food) <15:
        print("eaten")
        food.move()
        snake.new_seg()



screen.exitonclick()
