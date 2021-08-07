import sys
from secret_auction_art import logo
from os import system


def again():
    answer = input("Would you like to add another auctioneer? Yes/No:").lower()

    if answer == "yes":
        print("yes")
        system("clear")
        add_user()
    elif answer == "no":
        calculate_winner()
    else:
        print("Incorrect choice. Ending program.")
        sys.exit(0)


def add_user():
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    auctioneers.append({
        "name": name,
        "bid": bid,
    })

    again()


def calculate_winner():
    winner = {"name": "test", "bid": 0}

    for person in auctioneers:
        if person["bid"] > winner["bid"]:
            winner = {"name": person["name"], "bid": person["bid"]}

    print(f"The winner is {winner['name']} with a bid of {winner['bid']}")


print(logo)
print("Welcome to the Secret Auction!")
auctioneers = []

add_user()
