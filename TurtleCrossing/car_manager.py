COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle
class CarManager:
    def __init__(self):
        #super().__init__()
        self.cars = []
        self.make_car()
        #self.move_cars()

    def make_car(self):
        #for color in COLORS:
            #print(color)
            dice_wizard = random.randint(1,6)
            randy = random.randint(-280,280)
            if dice_wizard==1:
                car = Turtle("square")
                car.shapesize(stretch_wid=1, stretch_len=2)
                car.penup()
                car.color(random.choice(COLORS))
                car.goto(280, randy)
                car.setheading(180)
                self.cars.append(car)
                self.move_cars()
    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
