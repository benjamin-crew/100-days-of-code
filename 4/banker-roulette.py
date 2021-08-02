import random

names_string = input("Please enter everybodies names, seperated by a comma: ")

names = names_string.split(", ")
number = (len(names)) - 1

payee = names[random.randint(0, number)]
print(f"{payee}, you lose.")