from turtle import *
import random


cat = Turtle()
screen = Screen()
screen.bgcolor("grey")
cat.shape("turtle")
cat.color("deeppink")
colormode(255)
#cat.pencolor("blue")

def color_rand(t):
    first = random.randint(0, 255)
    second = random.randint(0, 255)
    third = random.randint(0, 255)
    return(first, second, third)


def dashed(t, amount):
    count = 0
    while count <amount:
        t.forward(10)
        t.up()
        t.forward(10)
        t.down()
        count +=1
def square(turtle, count =0):
    while count <4:
        turtle.forward(100)
        turtle.right(90)
        count +=1

def dash_square(turtle, count =0):
    while count <4:
        #turtle.forward(100)
        dashed(turtle, 10) # calls dashed line function inside square
        turtle.right(90)
        count +=1
#cat.forward(100)
#dashed(cat, 50)
#square(cat)
#cat.pencolor(color_rand(cat))
def calc_degrees(sides):
    """calculates number of degrees for each side of shape of numbered sides"""
    return (360/sides)

def shape(t, sides, count =0):
    """Takes in number of sides and turtle object to draw shape with that number sides"""
    t.pencolor(color_rand(t))
    deg = calc_degrees(sides)
    while count < sides:
        t.forward(100)
        t.right(deg)
        count +=1

def rand_walk(t, long):
    """returns a random path until it hits the length entered"""
    count = 0
    t.pensize(10)
    while count < long:
        t.pencolor(color_rand(t))
        t.forward(10)
        n = random.randint(0,3)
        if n==0:
            t.forward(10)
        elif n==1:
            t.right(90)
        elif n==2:
            t.left(90)
        elif n==3:
            t.backward(10)
        count +=1
def nested_shape(t):
    shape(t, 3)
    shape(t, 4)
    shape(t, 5)
    shape(t, 6)
    shape(t, 7)
    shape(t, 8)
    shape(t, 9)
    shape(t, 10)
rand_walk(cat, 100)

#triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

screen.exitonclick()