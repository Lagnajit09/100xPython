import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(display)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display:
  guess = input().lower()

  for i in range(0, len(chosen_word)):
    if chosen_word[i] == guess:
      display[i] = guess

  print(display)