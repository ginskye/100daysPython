#Band Name Generator - Day 1
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator!")

#2. Ask the user for the city that they grew up in.
city = input("Please enter the city you grew up in: \n")


#3. Ask the user for the name of a pet.
pet = input("Enter the name of a pet: \n")

#4. Combine the name of their city and pet and show them their band name.
print("Your band name is " + city + " "+ pet)
#5. Make sure the input cursor shows on a new line:

#Tip Calculator - Day 2
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator")
bill = input("Enter the amount of the bill ")
people = input("Enter the number of people dining ")
tip = input("Enter the percentage of tip ")
mult = 1 + (int(tip)/100)

result = round((float(bill)/int(people)) * mult, 2)
print(f"Each person should pay ${result}")

#Day 3 - Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("You are at a cross road.  What direction do you want to go? Left or Right? ").lower()
if direction=="left":
  lake = input("You come to a lake.  There is an island in the middle of the lake.  Type wait to wait for a boat, or swim to swim across ").lower()
  if lake=="wait":
    color = input("The boat arrives and a strange cat instructs your to get in.  He rows you to the island, where you see three houses, each with a different colored door - red, yellow, or blue. \n He tells you you must enter one of the houses and face what lies behind. \n  Choose your color  ").lower()
    if color=="yellow":
      print("You open the door to find an enormous library.  A talking crow tells you that books are of course the greatest treasure.")
    elif color=="red":
      print("No sooner do you open the door than you're devoured by a group of women with very sharp teeth.  Game Over.")
    else:
      print("The blue door opens to reveal an enormous pile of pillows, and a pride of sleepy tigers.  They invite you to their nap party, and you fall fast asleep.  Game over,")
  else:
    print("The waters are full of hungry eels, who quickly devour you.  Game over.")
else:
  print("The forest to your right is full of bloodthirsty crows, who quickly peck you to pieces.  Game over.")


#Day 4 - Rock, Paper Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
images = [rock, paper, scissors]

choice = int(input("Welcome to Rock, Paper Scissors!\n  Choose 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))

if (choice <0 or choice >2):
  print("Invalid choice, game over!")
else:
  print(f"You chose: {images[choice]}:")
  computer = random.randint(0,2)
  print(images[computer])
    
  if choice==computer:
    condition = "Draw"
  elif (choice==0 and computer ==1) or (choice==2 and computer==0) or (choice==1 and computer==2):
    condition = "Lose"
  else:
    condition = "Win"
  
  print(f"Your choice was {choice}")
  print(f"computer chose {computer} ")
  print(condition)

print("Thanks for playing!")

#Day 5 - Student Height Average
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
add = 0
count = 0
for h in student_heights:
    add +=h
    count +=1

avg = add / count
print(f"The average height is {round(avg)}")

#Day 5 Highest Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
biggest = 0
for s in student_scores:
    if s > biggest:
        biggest = s

print(f'The highest score in the class is: {biggest}')

#Calculate Sum of even numbers from 1 to 11 using the range function
total = 0
for n in range (2, 101, 2):
    total +=n
print(total)

#FizzBuzz
for n in range (1, 101):
    if n %5==0 and n %3==0:
        print("FizzBuzz")
    elif n % 5==0:
        print("Buzz")
    elif n%3==0:
        print("Fizz")
    else:
        print(n)


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pwlet = ""
pwsym = ""
pwnum = ""
for l in range(1, nr_letters+1):
  randlet = random.randint(0, 51)
  pwlet+=(letters[randlet])

for s in range(1, nr_symbols+1):
  randsym = random.randint(0,8)
  pwsym+=(symbols[randsym])

for n in range(1, nr_numbers+1):
  randnum = random.randint(0,9)
  pwnum+=(numbers[randnum])

print(pwlet+pwsym+pwnum)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#Dr Lu's solution is to create the password then shuffle arrangement
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
listpass = []
for l in range(1, nr_letters+1):
  listpass+=random.choice(letters)

for s in range(1, nr_symbols+1):
  listpass+=random.choice(symbols)

for n in range(1, nr_numbers+1):
  listpass+=random.choice(numbers) 
print(listpass)
random.shuffle(listpass)#inbuilt random.shuffle can mixup list items, but this can't be called inside a print statement
print(f'Your password is: {join(listpass)}')
  
