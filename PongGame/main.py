from ball import Ball
import turtle
import time
import paddle as p
from score import Scoreboard

screen = turtle.Screen()
screen.setup(800,600)
screen.title("Pong game")
screen.bgcolor("black")

screen.tracer(0)
screen.listen()

right_paddle = p.Paddle((350,0))
left_paddle = p.Paddle((-350,0))

ball = Ball()
board = Scoreboard()

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        print("hit wall")
        ball.y_bounce()
        #change direction
    #paddle collision
    if (ball.distance(right_paddle) <50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    if ball.xcor() > 380:
        board.update_l()
        ball.reset()

    if ball.xcor() < -380:
        board.update_r()
        ball.reset()

        #score

#start game
#static paddles
# ballwall collision



screen.exitonclick()