import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
screen.onkey(player.move_turtle, "Up")
cars = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.make_car()
    for car in cars.cars:
        if car.distance(player) <20:
            print("squash!")
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >=280:
        scoreboard.update_score()
        player.new_level()


screen.exitonclick()