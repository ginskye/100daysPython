import turtle as t
import random
etch = t.Turtle()
screen = t.Screen()
def forward():
    etch.forward(10)
def backward():
    etch.backward(10)
def clockwise():
    etch.right(10)
def counterclock():
    etch.left(10)
def clearscn():
    etch.clear()
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counterclock)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clearscn)
screen.exitonclick()
