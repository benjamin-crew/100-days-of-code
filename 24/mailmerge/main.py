PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

names_list = []
for name in names:
    names_list.append(name.strip("\n"))

for name in names_list:
    completed_letter = letter.replace(PLACEHOLDER, name)
    
    with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as file:
        file.write(completed_letter)