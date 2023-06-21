from turtle import Turtle

FONT = ("Arial", 24, "normal")
TOP = 0, 260

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        with open("./highscore.txt") as file:
            self.highest_score = int(file.read())

        self.score = 0
        self.goto(TOP)
        self.write(f"Score: {self.score}  High Score {self.highest_score}", align="center", font=FONT)


    def change_score(self):
        self.score +=1
        self.highest_score +=1
        self.clear()
        self.write(f"Score: {self.score}  High Score {self.highest_score}", align="center", font=FONT)

    def game_over(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        with open("./highscore.txt", mode="w") as file:
                file.write(f"{self.highest_score}")
        self.clear()
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 36, "normal"))
