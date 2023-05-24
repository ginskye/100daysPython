#reborg day 6
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

for x in range(0,6):
    jump()

#for random flag:
while at_goal()!=True:
    jump()

#for random course:
while at_goal()!=True:
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()  #comment out first line in jump() for this to work

#Maze navigation:
while at_goal()!=True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()

#Day8
#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    number = math.ceil((height * width) / cover)
    print(f"You'll need {number} cans of paint")

# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
    
#Day8 Prime Numbers
#Write your code below this line 👇
def prime_checker(number):
    prime = True
    for i in range (2, number):
        if number % i ==0:
            prime = False
    if prime==True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
  
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
