
from operator import ne


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Would you like to 'encrypt' or 'decrypt'?:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

text = list(text)
indexes = [alphabet.index(i) for i in text if i.isalpha()]
l = len(alphabet)

def encrypt(text,shift):
  rtrn_txt = []
  for i in indexes:
    total = i+shift
    if total >= l:
      remainingV = total % l
      ext_indx = alphabet[0+remainingV]
      rtrn_txt += ext_indx
    elif total <= l:
      rtrn_txt += alphabet[total]
  print(''.join(rtrn_txt))

def decrypt(text,shift):
  rtrn_txt = []
  for i in indexes:
    total = i-shift
    if total < 0:
      negSum = 0 - total
      ext_indx = alphabet[-negSum]
      rtrn_txt += ext_indx
    elif total <= l:
      rtrn_txt += alphabet[i-shift]
  print(''.join(rtrn_txt))

def enorde(direction):
  if direction == "encrypt":
    encrypt(text,shift)
  elif direction == "decrypt":
    decrypt(text,shift)

enorde(direction)


## got take into account punctuation.


    

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.