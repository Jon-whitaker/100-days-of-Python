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
input('You''re at a crossroad, where do you want to go? Type "left" or "right"')
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

# My Finished Hangman product:


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
word_list = [
"aardvark", 
"baboon", 
"camel",
"analytical",
"assess",
"conceptual",
"constitutional",
"creative",
"distribution",
"environmental",
"illegal",
"analyse",
"analysis",
"analyst",
"analytic",
"analyze",
"approach",
"area",
"assessment",
"assume",
"assumed",
"assuming",
"assumption",
"authoritative",
"authority",
"availability",
"available",
"beneficial",
"beneficiary",
"benefit",
"concept",
"conception",
"consist",
"consistency",
"consistent",
"consistently",
"constituency",
"constituent",
"constitute",
"constitution",
"constitutive",
"context",
"contextual",
"contextualize",
"contract",
"contractor",
"create",
"creation",
"creator",
"data",
"define",
"definition",
"derivation",
"derivative",
"derive",
"dissimilar",
"distribute",
"distributive",
"distributor",
"economic",
"economical",
"economically",
"economics",
"economist",
"economy",
"environment",
"environmentalist",
"establish",
"established",
"establishment",
"estimate",
"estimation",
"evidence", 
"evident",
"evidential",
"evidently",
"export",
"exporter",
"factor",
"finance",
"financial",
"financially",
"formula",
"formulate",
"formulation",
"function",
"functional",
"functionally",
"identifiable",
"identification",
"identify",
"identity",
"illegality",
"income",
"inconsistency"]
end_of_game = False
display = []
guessed_letters = []
chosen_word = random.choice(word_list)

for i in chosen_word:
  display += "_"

# print(chosen_word)

while end_of_game != True:
  try:
    guess = str(input("Guess a letter.\n")).lower()
    word_len = len(chosen_word)
    guessed_letters += guess

    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game == True
        print(f"Unfortunately '{guess}' isn't in there....You lost!\n\nThe word was {chosen_word}\n{stages[lives]}")
        break
      print(f"sorry, that guess is incorrect\n{stages[lives]}")

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

    dj = "".join(display)
    if end_of_game == False:
      print(f"These are the letters you've tried so far:\n{guessed_letters}\nYou have '{lives}' lives left, guess again..\n\n{dj}")
  except ValueError:
    print("Type in a letter")


#tried a letter already?







##-------------------------------------------------------------
##-------------------------------------------------------------

# How she did it






#Step 4

import random

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

end_of_game = False
word_list = [
"aardvark", 
"baboon", 
"camel",
"analytical",
"assess",
"conceptual",
"constitutional",
"creative",
"distribution",
"environmental",
"illegal",
"analyse",
"analysis",
"analyst",
"analytic",
"analyze",
"approach",
"area",
"assessment",
"assume",
"assumed",
"assuming",
"assumption",
"authoritative",
"authority",
"availability",
"available",
"beneficial",
"beneficiary",
"benefit",
"concept",
"conception",
"consist",
"consistency",
"consistent",
"consistently",
"constituency",
"constituent",
"constitute",
"constitution",
"constitutive",
"context",
"contextual",
"contextualize",
"contract",
"contractor",
"create",
"creation",
"creator",
"data",
"define",
"definition",
"derivation",
"derivative",
"derive",
"dissimilar",
"distribute",
"distributive",
"distributor",
"economic",
"economical",
"economically",
"economics",
"economist",
"economy",
"environment",
"environmentalist",
"establish",
"established",
"establishment",
"estimate",
"estimation",
"evidence", 
"evident",
"evidential",
"evidently",
"export",
"exporter",
"factor",
"finance",
"financial",
"financially",
"formula",
"formulate",
"formulation",
"function",
"functional",
"functionally",
"identifiable",
"identification",
"identify",
"identity",
"illegality",
"income",
"inconsistency"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])



##-------------------------------------------------------------
##-------------------------------------------------------------

# My best version:



import random
import hangman_words as hw
import hangman_art as ha
from replit import clear


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
    clear()
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
  
      elif guess in chosen_word:
        print(f"Excellent guess! '{guess}' is in there!\n")
      for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
          display[position] = letter
          if "_" not in display:
            end_of_game = True
            print(f"\nCongratulations!!!!!\n\n{ha.Win}\n\n you've Found the word is was '{chosen_word}'\n")
            break
          
        dj = " ".join(display)
      if end_of_game == False:
        print(f"These are the letters you've tried so far:\n{guessed_letters}\nYou have '{lives}' lives left, guess again..\n\n{dj}")
    else:
        if guess in guessed_letters:
          print(f"You've already guessed that Letter..\n {dj}\n....try again....")
  except ValueError:
    print("Type in a letter")





##-------------------------------------------------------------
##-------------------------------------------------------------


# poitional kwargs:
 def greet_with(name = "Jon", location = "Home"):
  print(f"Hi {name} ")
  print(f"What's your {location}? ")

  # the above is an example of a positional key word argument set, because as opposed to just entering (name, location) which could get mixed up, now we know that name goes first and location goes second.

##-------------------------------------------------------------
##-------------------------------------------------------------
#paint calculator.

  #Write your code below this line 👇

def paint_calc(height,width,cover):
  result = round((height*width)/cover)
  print(f"You'll need {result} cans of paint.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


##-------------------------------------------------------------
##-------------------------------------------------------------
# Prime number checker.

# To check for primes, you need to check the range of numbers up to the prime and see if any of the range devide into the number.

#Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



##-------------------------------------------------------------
##-------------------------------------------------------------

# Caesar cipher


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Would you like to 'encrypt' or 'decrypt'?:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

text = list(text)
# below creates an index number for each item in the list (text)
indexes = [alphabet.index(i) for i in text if i.isalpha()]
l = len(alphabet)

def encrypt(plain_text,shift_amount):
  rtrn_txt = []
  for i in indexes:
    total = i+shift_amount
    if total >= l:
      remainingV = total % l
      ext_indx = alphabet[0+remainingV]
      rtrn_txt += ext_indx
    elif total <= l:
      rtrn_txt += alphabet[total]
  print("Encoded text = "+(''.join(rtrn_txt)))

def decrypt(encrypted_text,shift_amount):
  rtrn_txt = []
  for i in indexes:
    total = i-shift_amount
    if total < 0:
      negSum = 0 - total
      ext_indx = alphabet[-negSum]
      rtrn_txt += ext_indx
    elif total <= l:
      rtrn_txt += alphabet[i-shift_amount]
  print("Your decypted text is: "+(''.join(rtrn_txt)))

def enorde(direction):
  if direction == "encrypt":
    encrypt(text,shift)
  elif direction == "decrypt":
    decrypt(text,shift)

enorde(direction)

##-----------------------------------

#How she did it:

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)

  
##-----------------------------------

# She combined the functions

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


##-----------------------------------
# So I had to give in with my attempt as it didn't work with indexes :(
  # I've moved on using her code.
  # below is as far as I got.


import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
direction = input("Would you like to 'encrypt' or 'decrypt'?:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

text = list(text)
# below creates an index number for each item in the list (text)
indexes = [alphabet.index(i) for i in text if i.isalpha()]
l = len(alphabet)

def caesar(direction, input_text, shift_amount):
  rtrn_txt = []    
  if direction == "en":
    for i in text:
      if str(i).isalpha() == False:
        rtrn_txt += str(i)
    for i in indexes:
      en_total = i+shift_amount
      if en_total >= l:
        remainingV = en_total % l
        ext_indx = alphabet[0+remainingV]
        rtrn_txt += ext_indx
      elif en_total <= l:
        rtrn_txt += alphabet[en_total] 
    print("Encoded text = "+(''.join(rtrn_txt)))
  elif direction == "de":
    for i in indexes:
      if i not in alphabet:
        rtrn_txt += i
      de_total = i-shift_amount
      if de_total < 0:
        negSum = 0 - de_total
        ext_indx = alphabet[-negSum]
        rtrn_txt += ext_indx
      elif de_total <= l:
        rtrn_txt += alphabet[i-shift_amount]
    print("Your decypted text is: "+(''.join(rtrn_txt)))

def encrypt(plain_text,shift_amount):
  rtrn_txt = []
  for i in indexes:
    total = i+shift_amount
    if total >= l:
      remainingV = total % l
      ext_indx = alphabet[0+remainingV]
      rtrn_txt += ext_indx
    elif total <= l:
      rtrn_txt += alphabet[total] 
  print("Encoded text = "+(''.join(rtrn_txt)))

def decrypt(encrypted_text,shift_amount):
  rtrn_txt = []
  for i in indexes:
    total = i-shift_amount
    if total < 0:
      negSum = 0 - total
      ext_indx = alphabet[-negSum]
      rtrn_txt += ext_indx
    elif total <= l:
      rtrn_txt += alphabet[i-shift_amount]
  print("Your decypted text is: "+(''.join(rtrn_txt)))

def enorde(direction):
  if direction == "en":
    encrypt(text,shift)
  elif direction == "de":
    decrypt(text,shift)

caesar(input_text=text, shift_amount=shift, direction=direction)


##-----------------------------------

#ok, my shot at her code:

from art import logo1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


proceed = True

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if shift_amount >= 26:
    y = shift_amount % 26
    shift_amount = y
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:

    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char.isalpha() == False:
      end_text += char
    else:
      position = alphabet.index(char)
      new_position = position + int(shift_amount)
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
while proceed == True:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
# Hint: Think about how you can use the modulus (%).

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  try_again = input("would you like to restart the cypher program? type: 'yes' or 'no'")
  if try_again == "no":
    proceed = False 

##-----------------------------------

# what she did.
''' this has a great while loop and she's simplified what I did with Modulo %'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    



##-------------------------------------------------------------
##-------------------------------------------------------------

# Dictionaries

# dictionaries are denoted by curly bracers {}
# to add to an existing dictionary, you'd do the following:

dict1 = {}
dict1["key"] = "value" # don't forget the key and value have to be in "quotes"
# so:
dict1["list1"] = "whatever this value needs to be"

# if you create the same dictionary further down, that also wipes the dictionary. 
# so if i were to create dict1 again below, it'd be empty.

dict1 = {}

# to edit a dict, you'd pick the same key as shown above, but asign a new value to it, and if you assign a key that's not there, it'll just create a new entry.

# looping through a dictionary:
# if you do a for loop, it'll just give you back the keys:
for key in dict1:
  print(key)

# so to print the key/value, you'd write:
for key in dict1:
  print(dict1[key]) # putting it in square brackets matters apparently


##-------------------------------------------------------------
##-------------------------------------------------------------

#grading exercise.


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

for key in student_scores:
  if student_scores[key] >= 91:
    student_grades[key] = "Outstanding"
  if student_scores[key] >= 81 and student_scores[key] <= 90:
    student_grades[key] = "Exceeds Expectations"
  if student_scores[key] >= 71 and student_scores[key] <= 80:
    student_grades[key] = "Acceptable"
  if student_scores[key] <= 70:
    student_grades[key] = "Fail"


#TODO-2: Write your code below to add the grades to student_grades.👇

# 🚨 Don't change the code below 👇
print(student_grades)

##-----------------------------------

# How she did it:

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  if score > 80:
    student_grades[student] = "Excee ds Expectations"
  if score >= 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"


##-------------------------------------------------------------
##-------------------------------------------------------------

# With dictionaries, you can't have multiple values per key, unless you nest the values inside a list or another dictionary:

travel_log = {
  "France": "Paris", "Normandy", "lille" #.. This doesn't work apparently
}

# Instead you'd have to have:

travel_log = {
  "France": ["Paris", "Normandy", "lille"]
}

# Nesting a dictionary or list inside another outer dictionary is more useful than nesting a list inside a list because of the way the data is structured

# Nesting a dictionary inside a dictionary:

travel_log = {
  "France": {"cities_visited": ["Paris", "Nor mandy", "lille"], "total_visits": 12}
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits" 32}
}

# The difference between accessing lists compared to dictionaries:
# Lists are accessed by their positional value.. so: list[0] etc
# dictionaries are accessed by their key/value data, so: dict1[key]

# Nesting a dictionary inside a list:
# when creating nested items, it's a good idea to separate them out:

travel_log = [
  {
    "country": "France", 
    "cities_visited": ["Paris", "Nor mandy", "lille"],
    "total_visits": 12
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits" : 32
  }
]

##-------------------------------------------------------------
##-------------------------------------------------------------

# adding a dictionary to an already existing list of dictionaries:

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(input_country, times_visited, cities_visited):
  travel_log.append({
      "country": input_country, 
      "visits": times_visited,
      "cities": cities_visited
  })


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

##--------------------------------

# how she did it:

def add_new_country(input_country, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = input_country
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visted
  travel_log.append(new_country)

  ##-----------------------------

# to print a specific item from a dictionary like the ones shown above, use:


# Question 3:
# Which line of code will print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
# [2] accesses the value with key 2, [0] gets the first item from the list.
print(order["main"][2][0])

##-------------------------------------------------------------
##-------------------------------------------------------------


# Secret auction program



from replit import clear
from art import logo2
from time import sleep
from hangman_art import Win

in_progress = True
bids = {}

def place_bid(name, bid):
  bids[name] = bid

def deets(seller,item):
  clear()
  print(logo2 +"\n")
  name = input(f"Whalecum to the blind auction! Today, you will be bidding for the glorious chance to own '{item}' being sold by '{seller}'.\nPlease enter your name, and let the bidding commence!\n")
  bid = int(input(f"Hi {name}, please enter your bid for '{item}' in £s\n"))
  bid_correct = input(f"Your bid was '£{bid}', is this correct? 'y/n'\n")
  if bid_correct == "y":
    place_bid(name, bid)
    next = input(f"congratulations, you're in the running to win '{item}' with a bid of '£{bid}', are you the last bidder? 'y/n'")
    if next == "n":
      print("Please pass the device over to the next bidder after the screen clears")
      print(sleep(3))
      clear()
      deets(seller,item)
    else:
      clear()
      max_bidder = [key for key, value in bids.items() if value == max(bids.values())]
      max_value = max(bids.values())
      print(f"Congratulations {max_bidder}!! You have won with a max bid of: £{max_value}")
      print(Win)
  else:
    deets(seller,item)

def start():
  print(logo2 +"\n")
  seller = input("Hi, As the initial seller, please can you enter your name.. \n")
  item = input(f"Hi {seller} what item would you like to sell? \n")
  deets(seller,item)

while in_progress:
  try:
    start()
    try_again = input("Would you like to auction anything else? 'y/n'")
    if try_again == "y":
      start()
    else:
      if try_again != "y":
        in_progress = False
  except:
      break

# when you use a for loop on a dictionary, it loops through each of the keys, not each of the key/values.
##----------------------------

# How she did it:

from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  

"""
FAQ: My console doesn't clear()

This will happen if you’re using an IDE other than replit. 
I’ll cover how to use PyCharm in Day 15. That said, you can write your own clear() function or configure your IDE like so: 

https://www.udemy.com/course/100-days-of-code/learn/lecture/19279420#questions/16084076

"""
# Mine is a bit more in depth than hers by the looks of it.

# the return function tells the computer to exit the program, so nothing after the return is actioned.

##-------------------------------------------------------------
##-------------------------------------------------------------

# leap year month days:

# my code:

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  leap_year = is_leap(year)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if leap_year == True:
    ly_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return ly_month_days[month-1]
  else:
    return month_days[month-1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

##-------------------------------

# How she did it:

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month > 12 or month < 1:
    return "invalid input"
  leap_year = is_leap(year)
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  return month_days[month -1]
    
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)



##-------------------------------------------------------------
##-------------------------------------------------------------


# docstrings:

#dockstrings are the explanations about what a function does when you tab.
# so for len() it displays what len actually does.
# we can create these in our functions by using 3x " on the line immediately after a def statement.. so for example:
def my_function():
   """this is a docstring and this is the location it should be in"""


##-------------------------------------------------------------
##-------------------------------------------------------------

# calculator function issue 1.01 - check out the notes for working with dictionaries.

# calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
  "+":add, 
  "-":subtract, 
  "*":multiply, 
  "/": divide
  }

num1 = int(input("What's the first number?: "))
for key in operations:
  print(key)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

# so to call a string input as a function we have to do the following:
calculation_function = operations[operation_symbol]
# now we can use the operation_symbol string as a function call... ffs.
first_answer = calculation_function(num1,num2)
# it wasn't working because I put in the values, in the dictionary as strings.. instead of function calls... it's the dictionary that pairs together the input and the function call.
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# Look how the code is almost cyclical, using the same functions and parameters over and over same name, same function, same operation, just used over and over.
operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

##-------------------------------

# This version shows a bug:

#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
  print(symbol)

#Here we select "+"
operation_symbol = input("Pick an operation: ") 
num2 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

#Here we select "*" which overides the "+" we selected on line 26.
operation_symbol = input("Pick an operation: ") 
num3 = int(input("What's the next number?: "))

#Here the calculation_function selected will be the multiply() function
calculation_function = operations[operation_symbol] 

#Here the code will be:
#second_answer = multiply(multiply(num1, num2), num3)
second_answer = calculation_function(calculation_function(num1, num2), num3)
#second_answer = 2 * 3 * 3 = 18
#To fix this bug we need to change the code on line 42 to:
second_answer = calculation_function(first_answer, num3)
#In the next lesson, we will delete all the code from line 34-48 so don't worry
#It won't affect your final project.
#But it's a good oportunity to practice debugging. 🐞

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")


##-------------------------------
# This is the finished version... check notes for how to cycle around.

from replit import clear 
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
# she's also created a function so she can start a new calculation. - recursion.
def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
# look at the below in particular to see how she cycles around. num1 = answer if input == "y"
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()

##-------------------------------------------------------------
##-------------------------------------------------------------


## BlackJack - 

# So this is as far as I got:

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




##-------------------------------------------------------------
##-------------------------------------------------------------


# Here's what she did:

