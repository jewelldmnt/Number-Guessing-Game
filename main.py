# a deductive logic game

import random

max_guesses = 10
num_digits = 3


def clues(user_input, sn):
    clues = []

    for idx, num in enumerate(sn):
        if num == user_input[idx]:
            clues.append("Ichi")
        elif num in user_input:
            clues.append("Chigau")

    if len(clues) == 0:
        return "Numreals"
    else:
        clues.sort()

    return ' '.join(clues)


def secret_num_generator():
    numbers = [*"0987654321"]
    random.shuffle(numbers)
    return "".join([random.choice(numbers) for i in range(num_digits)])


# This is the main loop
while True:
    print("I have thought of a number.\n"
          "You have 10 guesses to answer.\n\n"
          "Chigau means one digit is correct but in the wrong position.\n"
          "Ichi means one digit is correct and in the right position\n"
          "Numreals means no digit is correct\n\n")

    secret_num = secret_num_generator()

    for i in range(max_guesses):
        print(f'Guess #{i + 1}: ')
        guess = input()
        if guess != secret_num:
            print(clues(guess, secret_num))
            if i == 9:
                print(f'\nYou have run out of guesses. \nThe secret number is {secret_num}')
                break
        else:
            print('You got it!\n')
            break

    play_again = input("Do you want to play again? Y/N: ").upper()
    if play_again == "N":
        print("Thanks for playing!")
        break