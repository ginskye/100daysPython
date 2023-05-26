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


#Day 9 Grading exercise
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {

}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    student = key
    score = student_scores[key]
    if score >90:
        student_grades[student]="Outstanding"
    elif score >80 and score <90:
        student_grades[student]="Exceeds Expectations"
    elif score >70 and score <80:
        student_grades[student]="Acceptable"
    elif score <70:
        student_grades[student]="Fail"
# 🚨 Don't change the code below 👇
print(student_grades)

#Day9 - Travel Log
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, integer, cities):
    travel_log.append({"country": country, "visits": integer, "cities": [cities]})
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#day10 - days in month
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        #print("Leap year.")
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  """This is a docstring """
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year)==True and month==2:
      return 29
  else:
      return month_days[month-1]  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







