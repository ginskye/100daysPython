#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import art
import random
computer = random.randint(1, 101)
difficulty = ""
game = True
print(art.number_guess_logo)

while game==True:
  while difficulty !="easy" and difficulty !="hard":
    difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty.  Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
      guesses = 10
    elif difficulty=="hard":
      guesses= 5
    else:
      print("Please try again.")
  
  while guesses >0:
    guessed = int(input("Make a guess: "))
    guesses -=1
  
    if guessed==computer:
      print(f"You guessed correctly!")
      game=False
      break
    elif guessed > computer:
      print(f"Too high.\nGuess again.\nYou have {guesses} attempts remaining to guess the number")
    elif guessed < computer:
      print(f"Too low.\nGuess again.\nYou have {guesses} remaining to guess the number")

  if guesses==0:
    print(f"You've run out of time!  The number was {computer}")
    game=False


