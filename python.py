# This is simple Treasure game - that i designed on Python :) Have fun 

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_1 = input("Left or Right : Type L or R")
if first_1 == "L":
    second_2 = input("S or W")
    if second_2 == "W":
        third_3 = input("Which door R, B, Y")
        if third_3 == "Y":
            print("Win")
        elif third_3 == "R":
            print("Burned by Fire : Game Over")
        elif third_3 == "B":
            print("Eaten by beast : Game Over")
        else:
            print("Game Over")
    else:
        print("Attached by T : Game Over")
else:
    print("Fall into hole : Game Over")

# Rock Paper Scissors Game 
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
list = [rock,paper,scissors]
user_input = int(input("Choose 0 for Rock, 1 for paper and 2 for Scissor \n"))
computer_choice = random.randint(0,2)
if user_input > 2:
    print("Bad Choice, cant choose more then 2 : You loose \n ")
elif user_input == 0:
    print(f"User Choice: {rock} \n ")
elif user_input == 1:
    print(f"User choice: {paper} \n ")
elif user_input == 2:
    print(f"User Choice:  {scissors} \n ")
# Computer choose
print(f"computer choice: {list[computer_choice]} \n ")
# Comparision to check if computer wins or users

# Password generator


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Easy Way out
password = ""
#nr_letter = 4
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password = password + random_char

for char in range(1,nr_symbols + 1):
    random_sym = random.choice(symbols)
    password = password + random_sym

for char in range(1,nr_numbers + 1):
    random_num = random.choice(numbers)
    password = password + random_num
print(password)
if computer_choice > user_input:
    print("Computer Wins \n ")
elif user_input > computer_choice:
    print("You Wins \n ")
elif computer_choice == user_input:
    print("DRAW : Play again \n ")


#### hard level password generator 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# Easy Way out

## Hard Logic
password_list = []
#nr_letter = 4
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password_list.append(random.choice(letters))

for char in range(1,nr_symbols + 1):
    random_sym = random.choice(symbols)
    password_list.append(random.choice(symbols))

for char in range(1,nr_numbers + 1):
    random_num = random.choice(numbers)
    password_list.append(random.choice(numbers))
#print(password_list)
random.shuffle(password_list)
#print(password_list)

password = ""
for char in password_list:
    password += char
print(f"your password is : {password} \n ")
