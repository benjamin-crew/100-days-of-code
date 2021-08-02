import random
import sys

heads = 0
tails = 1

choice = (input("Choose [H]eads or [T]ails: ")).lower()

if choice == "h":
    choice_num = 0
elif choice == "t":
    choice_num = 1
else:
    print("Incorrect choice")
    sys.exit()

random_number = random.randint(0, 1)

if random_number == 0:
    print("Heads!")
else:
    print("Tails!")

if choice_num == random_number:
    print("Congrats, you win.")
else:
    print("You lose!")