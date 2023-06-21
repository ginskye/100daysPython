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

game_on = True
snake = s.Snake()
food = Food()
player_score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake.up()
while game_on:
    screen.update() #refresh screen
    time.sleep(0.1)
    snake.move()

    #collision detection


    if snake.head.distance(food) <15:
        scorenum = player_score.score
        #screen.update()
        player_score.change_score()
        #print(scorenum)
        food.move()
        snake.add_seg()

    #tail    collision
    for item in snake.segments[1:]:
        print(f"Index is: {snake.segments.index(item)}, distance from head is: {snake.head.distance(item)}")
#        print(snake.segments.index(item))
        if item == snake.segments[0]:
            #print(item)
            print(f"head {snake.segments.index(item)}")
        elif snake.head.distance(item) < 10:
            print(f"collide - distance is {snake.head.distance(item)}")
            game_on = False
            player_score.game_over()
        else:
            print("no collision")

    #detect wall collision
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_on = False
            player_score.game_over()


    #
    #screen.update()



screen.exitonclick()
