# if condition:
#   do this
# else:
#   do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

# Comparison Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

# = vs ==
# = is assigning a value to a variable
# == is checking equality

# Odd or Even
# % is modulo operator to find the remainder

number = int(input())

if(number % 2 == 0):
  print('This is an even number.')
else:
  print('This is an odd number.')


# Nested if/else
# if condition:
#   if another condition:
#     do this
#   else:
#     do this
# else:
#   do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if(height >= 120):
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if(age <= 18):
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

# if/elif/else
# if condition1:
#   do A
# elif condition2:
#   do B
# else:
#   do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if(height >= 120):
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if(age < 12):
    print("Please pay $5.")
  elif(age <= 18):
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

# BMI 2.0
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
bmi = weight / (height **2)

if(bmi < 18.5):
  print(f"Your BMI is {bmi}, you are underweight.")
elif(bmi < 25):
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif(bmi < 30):
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif(bmi < 35):
  print(f"Your BMI is {bmi}, you are obese.")
elif(bmi >= 35):
  print(f"Your BMI is {bmi}, you are clinically obese.")


# Leap year
# Which year do you want to check?
# Flow chart: https://shorturl.at/vS92r
year = int(input())

if(year % 4 == 0):
  if(year % 100 == 0):
    if(year % 400 == 0):
      print('Leap year')
    else: 
      print('Not leap year')
  else:
    print('Leap year')
else:
  print('Not leap year')


# Multiple if
# if condition1:
#   do A
# if condition2:
#   do B
# if condition3:
#   do C

# Flow chart: https://shorturl.at/f6Ii3
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if(height >= 120):
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if(age < 12):
    bill = 5
    print("Child tickets are $5.")
  elif(age <= 18):
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if(wants_photo == "Y"):
    bill += 3
  print(f"Your final bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride.")


# Logical operators
# A and B
# C or D
# not E


# Love calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if(score < 10 or score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score >= 40 and score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://shorturl.at/9biyp

#Write your code below this line 👇
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")