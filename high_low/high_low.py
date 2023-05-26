import art
from game_data import data
import random
print(art.logo)
user_score = 0

def roll_dice():
  return random.choice(data)
  
a = roll_dice()
b = roll_dice()
correct = True

def compare(input):
  numa = int(a["follower_count"])
  numb = (b["follower_count"])
  if numa >numb and input=="a":
    return True
  elif numb>numa and input=="b":
    return True
  else:
    return False

while correct:
  
  print(f"Compare A: {a['name']}, {a['description']} from {a['country']}")
  print(art.vs)
  print(f"Against B: {b['name']}, {b['description']} from {b['country']}")
  answer = input("Who has more followers?  Type 'A' or 'B': ").lower()
  result = compare(answer)
  if result==True:
    user_score+=1
    print(f"You're right! Current score: {user_score}")
    a = roll_dice()
    b = roll_dice()
  else:
    print(f"I'm sorry, that's not right.  Your score is: {user_score}")
    correct=False

