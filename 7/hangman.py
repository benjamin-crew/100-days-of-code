import random
import sys
from hangman_lists import word_list, stages, logo


def hangman(word_list):

    chosen_word = random.choice(word_list)
    lives = 6
    display = []

    for char in chosen_word:
        display.append("-")

    while lives > 0:

        in_string = False

        if "-" in display:
            guess = input("Guess a letter: ").lower()
            num = 0

            if guess in display:
                print(f"You've already got {guess}!")
            else:
                for char in chosen_word:
                    if char == guess:
                        display[num] = char
                        in_string = True

                    num += 1

                if in_string == False:
                    lives -= 1
                    print(stages[lives])
                    print(f"{guess} is not in word. Lives: {lives}")

            print(display)
            print(stages[lives])

        if "-" not in display and lives > 0:
            print("You win!")
            break

        if "-" in display and lives == 0:
            print("Out of lives. You lose!")
            print(f"The answer was: {chosen_word}")
            break


play = "yes"
print(logo)

while play == "yes":

    play = input("Would you like to play? Yes/No: ").lower()

    print(play)

    if play == "yes":
        hangman(word_list)
    elif play == "no":
        sys.exit()
    else:
        play = "yes"
        print("Incorrect answer.")
