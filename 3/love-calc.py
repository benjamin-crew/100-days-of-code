name_one = (input("What is your name: ")).lower()
name_two = (input("What is their name: ")).lower()
names = name_one + name_two

score_true = names.count('t') + names.count('r') + names.count('u') + names.count('e')
score_love = names.count('l') + names.count('o') + names.count('v') + names.count('e')

score = str(score_true) + str(score_love)
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you got together like coke and mentos.")
elif score > 39 and score < 51:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}.")