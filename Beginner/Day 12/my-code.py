import random

print("Welcome to the number guessing game!")
print("I am thinking a number between 1 and 100")

difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
number = random.randint(1,100)

if difficulty == 'easy':
  chances = 10
elif difficulty == 'hard':
  chances = 5

while chances > 0:
  print(f"\nYou have {chances} chances left to guess the number.")
  user_guess = round(float(input("Make a guess: ")))

  if user_guess == number:
    print(f"You got it! The number was {number}")
    break
  elif user_guess > number and user_guess - number > 15:
    print("Too high!")
    chances -= 1
  elif user_guess < number and number - user_guess > 15:
    print("Too low!")
    chances -= 1
  elif user_guess > number and user_guess - number < 10:
    print("High! You are close.")
    chances -= 1
  elif user_guess < number and number - user_guess < 10:
    print("Low! You are close.")
    chances -= 1

if chances == 0:
  print("You've run out of guesses, you lose.")