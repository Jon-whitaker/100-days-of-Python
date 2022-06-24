import random
import hangman_words as hw
import hangman_art as ha


stages = ha.stages
logo = ha.logo
lives = 7
word_list = hw.word_list
end_of_game = False
display = []
guessed_letters = []
chosen_word = random.choice(word_list)
print(logo)

for i in chosen_word:
  display += "_"

while end_of_game != True:
  try:
    guess = str(input("Guess a letter.\n")).lower()
    word_len = len(chosen_word)

    if guess not in guessed_letters:
      guessed_letters += guess    
         
      if guess not in chosen_word:
        lives -= 1
        if lives == 0:
          end_of_game == True
          print(f"Unfortunately '{guess}' isn't in there....You lost!\n\nThe word was {chosen_word}\n{stages[lives]}")
          break
        print(f"sorry, that guess is incorrect\n{stages[lives]}")
      
#      #--- indent the below
  
      elif guess in chosen_word:
        print(f"Excellent guess! '{guess}' is in there!\n")
      for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
          display[position] = letter
          if "_" not in display:
            end_of_game = True
            print(f"\nCongratulations, you've Found the word is was '{chosen_word}'\n")
            break
          
        dj = " ".join(display)
      if end_of_game == False:
        print(f"These are the letters you've tried so far:\n{guessed_letters}\nYou have '{lives}' lives left, guess again..\n\n{dj}")
    else:
        if guess in guessed_letters:
          print("You've already guessed that Letter.. try again")
  except ValueError:
    print("Type in a letter")
