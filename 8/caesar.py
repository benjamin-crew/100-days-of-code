from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(plain_text, shift_amount, cipher_direction):
    result_text = ""
    for char in plain_text:
        if char not in alphabet:
            result_text += char
        else:
            current_index = alphabet.index(char)
            if cipher_direction == "encode":
                new_index = (current_index + shift_amount) % 26
                result_text += alphabet[new_index]
            elif cipher_direction == "decode":
                new_index = (current_index - shift_amount) % 26
                result_text += alphabet[new_index]
            else:
                print("Invalid choice. Please choode encode or decode next time.")
                break

    return(result_text)


start = True

while start == True:
    replay = input("Would you like to start? Yes/No: ").lower()

    if replay == "yes":
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        print(caesar(text, shift, direction))
    else:
        start = False
