############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random
from replit import clear
from art import logo4
#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

player = input("\nWhat is your name?: \n")
print(f"Hi {player} Welcome to blackJack!\n")
print(logo4)

def deal_card(x):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  x.append(random.choice(cards))

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Create a list per player:
user_cards = []
computer_cards = []
playing = True
tally = 2
comp_tally = 2

def dealer(i,tally):
  while tally > len(i):
    deal_card(i)
    

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def calculate_score(x):
  tot = sum(x)
  if len(x) == 2 and tot == 21:
    return 0
  for i in x:
    if i == 11 and tot > 21:
      x.remove(i)
      x.append(1)
      return tot
  else:
    return tot

def compare(user_cards,computer_cards):
  if calculate_score(user_cards) >21 and calculate_score(computer_cards) > 21:
    print(f"Both you and the computer are bust!!\n")
    return False 
  elif calculate_score(computer_cards) > 21:
    print(f"You win {player} the computer bust!\n")
    return False
  elif calculate_score(user_cards) == calculate_score(computer_cards):
    print(f"You have the same score as the computer with {user_cards}, it's a draw!\n")
    return False
  elif calculate_score(user_cards) == 0:
    print(f"BlackJack!! Congratulations {player} you win!!\n")
    return False
  elif calculate_score(computer_cards) == 0:
    print("Computer has hit BlackJack, sorry, you lose.\n")
    return False
  elif calculate_score(user_cards) > 21:
    print(f"Sorry {player} you've bust! your score is: {calculate_score(user_cards)}\n")
    return False
  elif calculate_score(user_cards) > calculate_score(computer_cards):
    print(f"You win {player} with a score of {calculate_score(user_cards)}")
    return False
  elif len(user_cards) == 5 and calculate_score(user_cards) <= 21:
    print(f"Five card trick! nice, you win!\n")
  elif len(computer_cards) == 5 and calculate_score(computer_cards) <= 21:
    print(f"Five card trick! nice, computer wins!\n")
  else:
    print(f"The computer wins with a score of {calculate_score(computer_cards)}\n")
    return False


while playing:
  dealer(user_cards,tally)
  print(f"your cards are: {user_cards}\n")
  hit_me = input(f"your score is {calculate_score(user_cards)} do you want another card? y/n: ")
  if hit_me == "y":
    tally += 1
    if tally == 5:
      print(f"Five card trick! nice, you win!")
  elif hit_me == "n":
    print(f"your score is {sum(user_cards)}, it's now the computers turn.")
    clear()
    while calculate_score(computer_cards) < 17:
      dealer(computer_cards,comp_tally)
      comp_tally += 1
      print(f"The computers cards are: {computer_cards}\n")
      if calculate_score(computer_cards) >= 17:
        playing = compare(user_cards,computer_cards)

keep_playing = input("Would you like to play again? y/n: ")
if keep_playing == "y":
  playing = True
  tally = 2
  comp_tally = 2
  dealer(user_cards,tally)
else:
  print(f"Thanks for playing {player} come back soon!\n")
  playing = False

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#-------------------------------------

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.