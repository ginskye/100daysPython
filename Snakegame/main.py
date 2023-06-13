import time
import turtle as t
import Snake as s
from Food import Food
from scoreboard import Scoreboard
screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turns automatic animation off

segments = []
game_on = True
snake = s.Snake()
food = Food()
player_score = Scoreboard()

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
        scorenum = player_score.score
        screen.update()
        player_score.change_score(scorenum)
        print(scorenum)
        food.move()
        snake.new_seg()

    #detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        player_score.game_over()



screen.exitonclick()
