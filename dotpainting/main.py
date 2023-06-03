import turtle
from turtle import *
import random
import colorgram
dot_colors = colorgram.extract('hirstdots.jpg', 100)
turtle.colormode(255)
dot = Turtle()
#dot.setposition(0,0)
dot.pencolor("white")
#10 rows of 10 dots
dot.setx(-400.0)
dot.sety(-350.0)
#dot.backward(420)
dotnum = 0
row = 0
while row < 10:
    count = 0
    while count < 10:
        dot.shape("circle")
        dot.width(20)
        dot.color(dot_colors[dotnum].rgb)
        dot.stamp()
        dot.penup()
        dot.forward(90)
        count+=1
        dotnum +=1
        if dotnum==30:
            dotnum=0
    dot.setx(-400)
    new_coor = dot.ycor()+80
    dot.sety(new_coor)
    row +=1

screen = Screen()
screen.exitonclick()

def color_rand():
    first = random.randint(0, 255)
    second = random.randint(0, 255)
    third = random.randint(0, 255)
    return(first, second, third)

