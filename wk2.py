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
    