FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.color("black")
        self.level = 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def update_score(self):
        self.level +=1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

