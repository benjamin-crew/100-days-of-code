import pandas

data = pandas.read_csv("26/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
result = [phonetic_dict[letter] for letter in word]
print(result)