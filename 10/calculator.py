import sys
from calculator_art import logo


def add(n1, n2):
    return(n1 + n2)


def subtract(n1, n2):
    return(n1 - n2)


def multiply(n1, n2):
    return(n1 * n2)


def divide(n1, n2):
    return(n1 / n2)


def calculator():
    should_continue = True
    first_number = float(input("Pick a number: "))

    while should_continue is True:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        second_number = float(input("Pick a second number: "))

        function = operations[operation]
        answer = function(first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. Press anything else to exit: ").lower()
        if  choice == "y":
            first_number = answer
        elif choice == "n":
            should_continue = False
            calculator()
        else:
            print("Ending program.")
            should_continue = False

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
print(logo)
calculator()