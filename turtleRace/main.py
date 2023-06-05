import turtle as t
import random
#take user input for color
#display turtle race

screen = t.Screen()
screen.setup(500,400)
#user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win?  Enter a color: ")
#print(user_choice)
racers = []
def createRaceTurtle(color, pos):
    racer = t.Turtle(shape="turtle")
    racer.color(color)
    racer.penup()
    racer.goto(-240, pos)
    racers.append(racer)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
pos = -40
for color in colors:
    createRaceTurtle(color, pos)
    pos +=30
racing = True
while racing:
    dist = random.randint(0,10)
    for racer in racers:
        currentx = racer.xcor()
        #print(currentx)
        if currentx>=245:
            racing=False
            winner = racer
            print(winner)
        racer.forward(dist)


screen.exitonclick()