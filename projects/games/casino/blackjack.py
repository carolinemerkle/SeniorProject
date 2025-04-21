import random
#create deck 
cardCatagories = ["Hearts", "Diamonds", "Clubs", "Spades"]
cardList = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

deck = [(card, catagory) for catagory in cardCatagories for card in cardList]

#declare the values of the cards 
#ie set face card eqaul to 10
def cardValue(card):
  if card[0] in ["Jack", "Queen", "King"]:
    return 10
  elif card[0] == "Ace":
    return random.randint(1,11)
  else:
    return int(card[0])
#shuffle the deck 
random.shuffle(deck)

#deal the cards 
playerHand = [deck.pop(), deck.pop()]
dealerHand = [deck.pop(), deck.pop()]

while True:
  #
  player_score = sum(cardValue(card) for card in playerHand)
  dealer_score = sum(cardValue(card) for card in dealerHand)
  print("You have", playerHand)
  print("Your score is", player_score)
  print("\n")
  choice = input("Do you want to hit or stand? (h/s)").lower()
  if choice == "h":
    newCard = deck.pop()
    playerHand.append(newCard)
  #  player_score += cardValue(newCard)
    print(newCard)
  
  elif choice == "s": 
    break

  else:
    print("Invalid input. Please enter 'h' or 's'.")
    
    #determine if player busts
  if player_score > 21:
      print("You busted!")
      print("The house wins! \n You lose")
  break

 
    
#update dealer hand 
while dealer_score < 17:
  newCard = deck.pop()
  dealerHand.append(newCard)
  dealer_score += cardValue(newCard)
print("The house has", dealerHand)
print(dealer_score)
print("\n")

#determine winner
if dealer_score > 21:
  print("The house busted! \n You win!")
elif player_score > dealer_score:
  print("You win!")
elif dealer_score > player_score:
  print("The house wins! \n You lose")
else:
  print("You have ", player_score)
  print("the house has", dealer_score)
  print("The house wins!")
