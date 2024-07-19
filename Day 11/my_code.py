# Code
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_continue = True
while should_continue:

    restart = input("\nDo you want to play a game of Blackjack? Type 'Y' or 'N': ").lower()

    if restart != 'y':
        break

    user = []
    computer = []

    # Assign 2 random cards to each
    for i in range(2):
        user.append(random.choice(cards))
        computer.append(random.choice(cards))


    def blackjack():

        print(f"Your cards: {user}, Current score: {sum(user)} ")
        print(f"Computer's first card: {computer[0]} \n")

        if sum(user) == 21 and user == [11, 10]:
            print("You win!")
        elif sum(computer) == 21 and computer == [11, 10]:
            print(f"Computer's cards: {computer}, Current score: {sum(computer)} ")
            print("You lose!")
        else:
            if sum(user) > 21:
                if 11 not in user:
                    print("You lose!")
                else:
                    user[user.index(11)] = 1
                    if sum(user) > 21:
                        print("You lose!")
            else:
                draw_more = input("Type 'Yes' to get another card or 'No' to pass: ").lower()

                if draw_more == 'yes':
                    user.append(random.choice(cards))
                    blackjack()
                else:
                    while sum(computer) < 17:
                        computer.append(random.choice(cards))

                    print(f"Your final hand: {user}, Final score: {sum(user)} ")
                    print(
                        f"Computer's final hand: {computer}, Final score: {sum(computer)} "
                    )

                    if sum(computer) > 21:
                        print("You win!")
                    else:
                        if sum(computer) < sum(user):
                            print("You lose!")
                        elif sum(computer) > sum(user):
                            print("You win!")
                        else:
                            print("Draw!")


    blackjack()
