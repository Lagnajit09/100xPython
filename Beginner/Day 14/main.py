import random
import art
from game_data import data
# from replit import clear


def get_random_choices(first):
  random_choice = random.choice(data)

  while random_choice == first:
    get_random_choices(random_choice)

  return random_choice


def game(first, score, game_over=False):
#   clear()
  print(art.logo)

  if game_over:
    print(f"Sorry, that's wrong! Final score: {score}")
    return

  second = get_random_choices(first)

  if score != 0:
    print(f"You are right! Current score: {score}")
  
  print(f"Compare A: {first['name']}, {first['description']}, from {first['country']}")
  print(art.vs)
  print(f"Against B: {second['name']}, {second['description']}, from {second['country']}")

  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

  if user_choice == 'a' and first['follower_count'] >= second['follower_count']:
    game(second, score + 1)
  elif user_choice == 'b' and first['follower_count'] <= second['follower_count']:
    game(second, score + 1)
  else:
    game(second, score, True)
  

first = data[random.randint(0, len(data) - 1)]
score = 0
game(first, score)




