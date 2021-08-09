import sys
import random

EASY_MODE = 10
HARD_MODE = 5

print("Welcome to the Number Guessing Game!")


def set_difficulty(mode):
    """ Function to set amount of attempts."""
    if mode == 'easy':
        return EASY_MODE
    elif mode == 'hard':
        return HARD_MODE
    else:
        print("Incorrect input.")
        sys.exit(1)

def play():
    """Main play loop."""
    attempts = set_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())

    print(attempts)
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1, 100)

    while attempts > 0:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess == number:
            print("You win!!!")
            sys.exit(0)
        elif guess > number:
            print("Too high.")
            attempts -= 1
            print(f"Attempts left: {attempts}.")
        elif guess < number:
            print("Too low.")
            attempts -= 1
            print(f"Attempts left: {attempts}.")
        else:
            print("Incorrect input.")
            sys.exit(1)
    
    if attempts == 0:
        print("You lose!")
        sys.exit(0)

play()