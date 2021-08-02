import random

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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = random.randint(0, 2)

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 0:
    if computer_choice == 1:
        print(paper)
        print("Computer wins! Paper beats rock!")
    elif computer_choice == 2:
        print(rock)
        print("You win! Rock beats scissors!")
elif user_choice == 1:
    if computer_choice == 2:
        print(scissors)
        print("Computer wins! Scissors beats paper!")
    elif computer_choice == 0:
        print(paper)
        print("You win! Paper beats rock!")
elif user_choice == 2:
    if computer_choice == 0:
        print(rock)
        print("Computer wins! Rock beats scissors!")
    elif computer_choice == 1:
        print(scissors)
        print("You win! Scissors beats paper!")
elif user_choice not in [0, 1 ,2]:
    print("Incorrect choice.")