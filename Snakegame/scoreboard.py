from turtle import Turtle

FONT = ("Arial", 24, "normal")
TOP = 0, 260
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(TOP)
        self.write(f"Score: {self.score}", align="center", font=FONT)


    def change_score(self, score):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 36, "normal"))
