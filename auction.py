from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.auction_logo)
bids = {}
newbids  = True
highest = 0
person = ""
while newbids==True:
  name = input("Please enter your name: \n")
  bid = int(input("Please enter your bid: \n"))
  bids[name] = bid
  others = input("Are there other users who want to bid?  Enter yes or no:\n").lower()
  if others=="yes":
    clear()
  else:
    newbids=False

for val in bids:
  if bids[val] > highest:
    highest= bids[val]
    person = val
  
print(f"{person} has the high bid of ${highest}")


