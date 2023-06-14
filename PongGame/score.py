from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.goto(-100, 200)
        self.write_score()
        print("score initialized")


    def write_score(self):
       self.write(f"Left score: {self.left_score}  Right Score: {self.right_score}", align="center", font=("Courier", 20, "normal"))
       #self.write(f"Right Score: {self.right_score}", align="right", font=("Arial", 24, "normal"))

    def update_r(self):
        self.left_score +=1
        print(self.left_score)
        self.clear()
        self.write_score()

    def update_l(self):
        self.right_score +=1
        self.clear()
        self.write_score()
        print(self.right_score)
