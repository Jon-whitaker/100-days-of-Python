# to print over multiple lines, you can do:
print("text")
print("text")
# or 
print ("text line 1\ntext line 2")

## the above will print out the same thing over two separate lines.


# to concatenate two words or lines you use the + character.
print("hello" + " you!")

# to print out speech marks, you have to print them within the different speech mark types..
# for instance:
print('Id like to add together this sentence " "and this sentence" using the "+" ')
print('String concatenation is done with the "+" sign')


# for a user to input data, they use the "input" function:
name = input("what is your name? ")
print("Hello " + name)

def name_length(x):
  print(len(x))

name_length(Jon)


#How she did it
print(len(input("what is your name? ")))

## try nesting the functions instead of using def.

##-------------------------------------------------------------
##-------------------------------------------------------------


#to switch variables around you have to create a placeholder first:
# think about it as cups.. if you had two full cups, and you wanted to switch the contents around, then you'd need a third cup to transfer to first.

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


#no numbers at the start of vars or spaces in the names of vars

##-------------------------------------------------------------
##-------------------------------------------------------------

# adding two numbers:

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

a = int(two_digit_number[0])
b = int(two_digit_number[1])
result = a + b
print(result)

##-------------------------------------------------------------
##-------------------------------------------------------------

## it wanted BMI with no decimal places.. so:

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

flt_height = round(float(height),1)
sq_height = flt_height **2
bmi = int(weight)/sq_height
int_bmi = int(bmi )
print(int_bmi)
 
##---------------------------------

#Here's how she did it:

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi)

##-------------------------------------------------------------
##-------------------------------------------------------------

// #two division symbols = floor division.
    ## this is used when dividing two numbers, instad of getting a float, you get a whole number rounded.

/= 
-= ## these are all ways to manipulate the previous value by whatever's in front.
+=

 10 /= 2 (5)
 10 -= 2 (8)
 10 += 2 (12)

##-------------------------------------------------------------
##-------------------------------------------------------------

 
#f-Strings

# When trying to print() if the data types don't match, you have to convert one of the non-printable data-types to a type that can print.. for instance changing an interger to a string with str().

# an F-string, makes it so you don't have to convert a data-type first (be it a float/int/bool) and to use these, you have to place an "f" at the beginning of your string before the quotes and then alias the non-string in via curly bracers {}:

score = 12
height = 1.8
isWinning = True

f"your score is {score}, your height is {height} and you are winning I think? {isWinning}"

##-------------------------------------------------------------

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f" You have {days_left} days, {weeks_left} weeks, or {months_left} months left until you're 90")

##-------------------------------------------------------------
##-------------------------------------------------------------

#Modulo

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
  print("This is an even number.")
else:
  print ("This is an odd number.")

##-------------------------------------------------------------
##-------------------------------------------------------------
#BMI 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

sq_height = height **2
bmi = round(weight/sq_height)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi <= 25.0:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25.0 and bmi <= 30.0:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30.0 and bmi <= 35.0:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35.0:
  print(f"Your BMI is {bmi}, you are clinically obese.")


##-------------------------------------------------------------
##-------------------------------------------------------------

## Leap year check

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0 and year % 100 != 0:
  print("Leap year.")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
  print("Leap year.")
else:
  print("Not leap year.")


##-------------------------------

# How she did it:

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap Year")
    else:
      print("Not a leap year.")
  else:
    print("Leap Year")
else:
  print("Not a leap year.")

##-------------------------------------------------------------
##-------------------------------------------------------------

#Pizza order

# 🚨 Don't change the code below 👇
from tkinter import Y


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


Small_Pizza: 15
Medium_Pizza: 20
Large_Pizza: 25
Small_Pep: 2
Pepperoni: 3
Extra_cheese: 1

total = 0

if size == "S":
  total += 15
elif size == "M":
  total += 20
elif size == "L":
  total += 25

if add_pepperoni == "N":
  pass
elif add_pepperoni == "Y" and size == "S":
  total += 2
elif add_pepperoni == "Y" and size == "M" or size == "L":
  total += 3

if extra_cheese == "N":
  pass
elif extra_cheese == "Y":
  total += 1

print(f"Your final bill is: ${total}.")


##------------------------------

#How she did it:


Small_Pizza: 15
Medium_Pizza: 20
Large_Pizza: 25
Small_Pep: 2
Pepperoni: 3
Extra_cheese: 1

total = 0

if size == "S":
  total += 15
elif size == "M":
  total += 20
elif size == "L":
  total += 25

if add_pepperoni == "Y":
  if size == "S":
    total =+ 2
  else:
    total += 3 

if extra_cheese == "Y":
  total += 1

print(f"Your final bill is: ${total}.")


##-------------------------------------------------------------
##-------------------------------------------------------------

# Nested If statements.

bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("Please pay £5.") 
  elif age <= 18:
    bill = 7
    print("Please pay £7.")
  elif age >= 45 and age <= 55:
    print("congratulations, you ride for free!")
  else:
    bill = 12
    print("Please pay £12.")
  
  wants_photo = input("Do you want a photo taken? Y or N")
  if wants_photo == "Y":
    #Add £3 to bill
    bill += 3

  print(f"Your final bill is £{bill}")
  
else:
  print("Sorry, you have to grow taller before you can ride.")



##-------------------------------------------------------------
##-------------------------------------------------------------


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


tl1 = ["t","r","u","e"]
tl2 = ["l","o","v","e"]
namz = name1 + name2
naml = namz.strip().lower()

score1 = 0
score2 = 0

for i in tl1:
  score1 += naml.count(i)

for i in tl2:
  score2 += naml.count(i)

if score1 < 1 or score1 >= 9:
  print(f"Your score is {score1}{score2}, you go together like coke and mentos.")
elif score1 == 4 or score1 == 5:
  print(f"Your score is {score1}{score2}, you are alright together.")
else:
  print(f"Your score is {score1}{score2}.")

##---------------------------

#How she did it:
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))



print(love_score)


if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")

##-------------------------------------------------------------
##-------------------------------------------------------------

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇

if round(test_seed) <= 5000:
  print("Tails")
else:
  print("Heads")

#----------------------
#what she did:

import random
random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")


##-------------------------------------------------------------
##-------------------------------------------------------------

#So this was an assignment to see who, out of a list of people, would pay for a food bill.
# it's random, based on the seed number.. 
# my solution takes the list length and divides it by 10, it then takes a rounded version of the random.random() test-seed, to 1 dec'place and multiplies the two by each other and again by 10 to get the list number
# then because lists start counting at 0, it minus's one from the number and calls print for the name in the list at that number.. 
# apparently this isn't good enough /shrug.



import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#this was my first try.
# print(f"{names[random.randint(0,len(names))]} is going to buy the meal today!")

# I could have just done the above with a -1 (sigh) - this version passed too.
#unfortunately I forgot that lists start counting at 0.
print(f"{names[random.randint(0,len(names))-1]} is going to buy the meal today!")

##--------------------------------
# instead of :
l = len(names) / 10
t = round(random.random(),1)
x = int(round((l*t)*10))
print(f"{names[x -1]} is going to buy the meal today!")

##--------------------------------

# so here's how she did it:


#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

##-------------------------------------------------------------
##-------------------------------------------------------------

#Good text tip:
# if you want to use quotes in an input message, but the computer thinks you're starting and finishing a string, half way through the sentence... i.e.:
input("You're at a crossroad, where do you want to go? Type "left" or "right".")
#So usually, to get around the issue shown above, we'd use a single quote at each end:
input('You're at a crossroad, where do you want to go? Type "left" or "right"'.)
#as shown, it's not working here because of the apostrophe in the work "you're"..
# so to combat this, we use a backslash to escape the apostrophe in you're:
input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()
# Et Vóila!


##-------------------------------------------------------------
##-------------------------------------------------------------
#Lists:

# To create a list:

cars = [] # use square brackets to create a list.
cars = ["fiesta", "BMW 320d", "Mercedes C Class", "Volvo XC90",]
# to index the list we use slice:
print(cars[1])
#to index from the last entry, we use minus.
print(cars[-1])
# to replace an entry we use index and change it with an equals
cars[2] = "Bugatti Veron"
# to add to the end of a list we use .append
cars.append("Audi A4")
# for more info, check out python data structures.
# another option is .extend, this allows you to append one list to another:
vans = ["ford transit", "mercedes sprinter", "vw transporter", "vauxhall vivaro",]
cars.extend(vans)

# Nested lists or lists of lists.
# If you have more than one list in a list.. and you wanted to print out the first item from the first list, you'd type:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[0][0]) # this prints out the first item from the first list as it's indexing the first list, and the first item in that list.

# if I wanted to print out the second item in the list, we'd type:

print(dirty_dozen[0][1])
#again, first list [0] and second item [1]
#if we wanted the third item in the second list say, we'd type:
print(dirty_dozen[1][2])

# pretty cool.


##-------------------------------------------------------------
##-------------------------------------------------------------

# Co-ordinates.

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

x = int(position[1]) -1
y = int(position[0]) -1
map[x][y] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")



##-------------------------------------------------------------
##-------------------------------------------------------------
# Rock,  Paper, Scissors.


import random

try:
  player_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for  Scissors: "))
except ValueError:
  print("\nWRONG!!.. you need to type a number doofus!\n")



computer_choice = random.randint(1, 3)

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# rock/scissors = 1/3 - win
# paper/rock = 2/1 = win
# scissors/paper = 3/2 - win

choices = {1:rock, 2:paper, 3:scissors}

# Put them in a dictionary?

try:
  if player_choice < 1 or player_choice > 3:
    print("You typed an invalid response, please try again.")
  elif player_choice == computer_choice:
    print(f"\nIt's a draw!\n\nYou chose:\n{choices[player_choice]}\nand the computer chose:\n   {choices[computer_choice]}\nPlease play again!\n")
  elif player_choice == 1 and computer_choice == 3:
    print(f"\nYou Win!\nYou chose:\n{choices[player_choice]}\nComputer chose:\n{choices   [computer_choice]}\n")
  elif player_choice == 2 and computer_choice == 1:
    print(f"\nYou Win!\nYou chose:\n{choices[player_choice]}\nComputer chose:\n{choices   [computer_choice]}\n")
  elif player_choice == 3 and computer_choice == 2:
    print(f"\nYou Win!\nYou chose:\n{choices[player_choice]}\nComputer chose:\n\n{choices   [computer_choice]}\n")
  else:
    print(f"\nSorry, you lose!\nYou chose:\n{choices[player_choice]}\nComputer chose:\n   {choices[computer_choice]}")
except NameError:
  print("")

  
##---------------------------------
# How she did it:

import random

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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end



##-------------------------------------------------------------
##-------------------------------------------------------------

#Average Height

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sh = 0
for i in student_heights:
  sh += i
  ah = round(sh / len(student_heights))
print(ah)


#180 124 165 173 189 169 146

#apparently I wasn't supposed to use the len() function.. oops.. 
# still, in order to use a for loop, I'd have just have to have incremented a counter for every entry in student_heights.

##-------------------------------

#Highest scores

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


highest = 0
for i in student_scores:
  if i > highest:
    highest = i
print(f"The highest score in the class is: {highest}")



##-------------------------------------------------------------
##-------------------------------------------------------------

# Range function:

for number in range(1,11, 2):
  print(number)

# with the example above, for the end of the range, you have to go one digit beyond.
# default is every number, or step.. however you can define the step by adding the third number on the end.


##-------------------------------------------------------------

#Write your code below this row 👇
total = 0

for i in range(0,101):
    if i % 2 == 0:
        total += i
print(total)

for i in range(0,101, 2):
    total += i
print(total)

##-------------------------------------------------------------
##-------------------------------------------------------------


#fizzbuzz

for i in range(1,101):
  if (i % 5 == 0 and i % 3 == 0):
    print("FizzBuzz")
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0:
    print("Fizz")
  else:
    print(i)


##-------------------------------------------------------------
##-------------------------------------------------------------



#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# Need to pick the length of the password.
# need to pick N x letters and N x numbres then for the amount of whatever's left with regards the length of the password, the computer needs to randomly pick the fill.

pswd = []

for i in range(nr_letters):
  pswd += random.choice(letters)
for i in range(nr_symbols):
  pswd += random.choice(symbols)
for i in range(nr_numbers):
  pswd += random.choice(numbers)

random.shuffle(pswd)
ps = "".join(pswd)
print(f"Your password is: " {ps})


  



##-------------------------------------------------------------
##-------------------------------------------------------------

# Found something very interesting with strings.. 
# if you turn a string into a list using just the square brackets, then it stays as one string:

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# i.e: 

cw = [chosen_word]
# will print out:
['aardvark']

# However, if we instead use the "list" function, then it will separate out each letter in the word automatically.
# i.e: 
list(chosen_word)
# will print out:
['a', 'a', 'r', 'd', 'v', 'a', 'r', 'k']



##-------------------------------------------------------------
##-------------------------------------------------------------

# This is how I started doing it:
import random

# Generate a random word
# Generate as many blanks as letters in the word
# Ask the user to guess a letter
# Is the guessed letter in the word?
# yes/no?
# if yes; replace the blank with a letter, 
# if no; lose a life -- have they run out of lives? no? guess again, yes... game over.
# are all the blanks filled? no -> guess again, yes => game-over

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

try:
  guess = str(input("Guess a letter.\n")).lower()
except ValueError:
  print("Type in a letter")
chosen_word = random.choice(word_list)
blank = ""
blank += "_" * len(chosen_word)
guessed_letters = []
guessed_letters = guessed_letters.append(guess)
s = [pos+1 for pos, char in enumerate(chosen_word) if char == guess]
t = [pos for pos, char in enumerate(chosen_word) if char == guess]

for i in t:
  blank = blank[:i] + guess + blank[i + 1:]
print("\n"+blank)
print("\n"+chosen_word)

# print(f"Your guess was '{guess}', and it's in there at position: {s}\nHere's the result:\n{blank}")


##-------------------------------------------------------------
##-------------------------------------------------------------


# This is how she's done it

# this is a better way because we're changing items in a list, as opposed to having to change a string.

display = []

for i in chosen_word:
  display += "_"
print(display)


for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter




##-------------------------------------------------------------
##-------------------------------------------------------------

# My Finished product:




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
