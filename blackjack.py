############### Blackjack Project #####################

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import art
import random
print(art.blackjack_logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  card = random.randint(1,13)
  return cards[card-1]

def calculate_score(card_list):
  #card_sum = sum(card_list)
  if sum(card_list)==21 and len(card_list)==2:
    return 0
  elif sum(card_list) >21:
    if 11 in card_list:
      card_list.append(1)
      card_list.remove(11)
      return sum(card_list)
    else:
       return sum(card_list)
  else:
    return sum(card_list)

def compare(user_score, computer_score):
  if user_score==computer_score:
    return "Draw"
  elif computer_score==0 or user_score >21 or computer_score > user_score:
    return "User loses"
  elif user_score==0 or user_score > computer_score:
    return "User wins!"
  elif computer_score >21:
    return "Dealer loses"
    
user_cards = []
computer_cards = []
game = True
#deal 2 cards:
for i in range(0,2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

while game == True:
  
    playscore = calculate_score(user_cards)
    compscore = calculate_score(computer_cards)

    if playscore==0 or compscore==0 or playscore >21: 
        print(compare(playscore, compscore))
        game = False

    else:
        print(f"Your cards are {user_cards}, current score is {playscore}")
        print(f"Dealer's first card is {computer_cards[0]}")
        #print(compscore)

        if playscore <21:
            draw = input("Would you like to draw another card? \n").lower()
            if draw=="yes":
                user_cards.append(deal_card())
                playscore = calculate_score(user_cards)
                print(playscore)
            else: 
                game= False
        else:
           game = False
        
        while compscore !=0 and compscore < 17:
            computer_cards.append(deal_card())
            compscore = calculate_score(computer_cards)
            #print(compscore)

print(f"Final Dealer cards: {computer_cards} and score was {compscore}")
print(f"Your final cards were: {user_cards} and your ending score was {playscore}")
print(compare(playscore, compscore))



#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

