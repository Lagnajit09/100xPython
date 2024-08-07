import random

stages = [
    '''
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
'''
]

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1.
#If lives goes down to 0 then the game should stop and it should print "You lose."

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    if guess not in chosen_word:
        lives -= 1
    else:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess

    print(display)
    print(stages[lives])

    if lives == 0:
        end_of_game = True
        print("You lose!")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
