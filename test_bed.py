import random

# Generate a random word
# Generate as many blanks as letters in the word
# Ask the user to guess a letter
# Is the guessed letter in the word?
# yes/no?
# if yes; replace the blank with a letter, 
# if no; lose a life -- have they run out of lives? no? guess again, yes... game over.
# are all the blanks filled? no -> guess again, yes => game-over


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 7
word_list = ["aardvark", "baboon", "camel"]
end_of_game = False
display = []
guessed_letters = []
chosen_word = random.choice(word_list)

for i in chosen_word:
  display += "_"

if "_" not in display:
  end_of_game = True
  print(f"\nCongratulations, you've Found the word is was '{dj}'\n")




while end_of_game != True:
  try:
    guess = str(input("Guess a letter.\n")).lower()
    word_len = len(chosen_word)
    guessed_letters += guess

    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game == True
        print(f"Unfortunately '{guess}' isn't in there....You lost!\n {stages[lives]}")
        break
      print(f"sorry, that guess is incorrect\n{stages[lives]}")
    if guess in chosen_word:
      print(f"Excellent guess! '{guess}' is in there!\n")
    for position in range(word_len):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
    dj = "".join(display)
    print(f"These are the letters you've tried so far:\n{guessed_letters}\nYou have '{lives}' lives left, guess again..\n\n{dj}")
  except ValueError:
    print("Type in a letter")


#tried a letter already?

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."


#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.



