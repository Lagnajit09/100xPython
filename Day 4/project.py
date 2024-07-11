# Rock, Paper, Scissors
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

symbols = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user > 2 or user < 0:
  print("You typed an invalid number, you lose!")
else:
  print(symbols[user])
  
  computer = random.randint(0,2)
  print('Computer chose: ')
  print(symbols[computer])
  if (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("You win!")
  elif user == computer:
    print("Draw!")
  else:
    print("You lose!")