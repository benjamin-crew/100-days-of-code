from art import logo, vs
from game_data import data
import random
import sys


def play():
    # Shuffle the data
    random.shuffle(data)

    # Keep score
    score = 0

    # Null the variables
    a = None
    b = None
    winner = None

    playing = True

    while playing is True:

        if winner != None:
            a = winner
        else:
            a = random.choice(data)
            
        b = random.choice(data)

        print(f"{a['name']}, {a['description']}, {a['country']}")
        print(vs)
        print(f"{b['name']}, {b['description']}, {b['country']}")

        guess = ""
        while guess != "a" and guess != "b":
            guess = input("\nWho has the most followers? A or B: ").lower()
            if guess != "a" and guess != "b":
                print("Invalid answer, try again.")

        if a['follower_count'] > b['follower_count']:
            answer = "a"
            winner = a
        elif a['follower_count'] < b['follower_count']:
            answer = "b"
            winner = b

        if guess == answer:
            score += 1
            print(f"\n{winner['name']} is correct! Score: {score}\n")
        else:
            print(f"\nWrong! Final Score: {score}")
            playing = False

        if score == len(data):
            print(f"\nFinal Score: {score}")
            print("\nYou've exhausted the list.")
            sys.exit()


print(logo)

play()
