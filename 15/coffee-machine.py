import sys


def check_resources(coffee):
    """Checks whether there are enough resources to make coffee"""

    enough_resources = True

    if "milk" in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
            enough_resources = False

    if(MENU[coffee]["ingredients"]["water"] > resources["water"]) and (MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]):
        enough_resources = False

    return(enough_resources)


def make_coffee(coffee):
    "Subtracts coffee ingredients from resources"
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]

    print(f"Here is your {coffee}.")


def check_money(choice, money):
    "Checks the user has enough money to buy coffee"
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    pennie = 0.01

    quarters_ammount = float(input("How many quarters?: "))
    dimes_ammount = float(input("How many dimes?: "))
    nickles_ammount = float(input("How many nickles?: "))
    pennies_ammount = float(input("How many pennies?: "))

    money += (quarter * quarters_ammount) + (dime * dimes_ammount) + \
        (nickle * nickles_ammount) + (pennie * pennies_ammount)
    print(f"Quarters: {quarters_ammount}, Dimes: {dimes_ammount}, Nickles: {nickles_ammount}, Pennies: {pennies_ammount}, Total: {money}")

    if MENU[choice]["cost"] > money:
        print("Sorry that's not enough money. Money refunded.")
        money = 0
    else:
        resources["money"] += MENU[choice]["cost"]
        money -= MENU[choice]["cost"]
        money = round(money, 2)
        print(resources["money"])
        print(f"Here is your change: {money}")
        money = 0

    make_coffee(choice)


def make_choice(money):
    """Ask what they would like"""
    loop = True
    while loop is True:
        choice = input("What would you like: ").lower()
        if choice != "espresso" and choice != "latte" and choice != "cappuccino":
            print("Incorrect choice")
        else:
            loop = False

    enough_resources = (check_resources(choice))

    if enough_resources:
        check_money(choice, money)
    else:
        print("Coffee machine out of resources. Switching off.")
        sys.exit()


# Varibles
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
money = 0


# print menu and costs
for x in MENU:
    print(f"{x}: {MENU[x]['cost']}")

# Ask if user wants coffee
active = True
while active is True:
    answer = input("Would you like a coffee? Yes/no: ").lower()
    if answer == "yes":
        make_choice(money)
    elif answer == "no":
        active = False
    elif answer == "off":
        print("Switching the machine")
        sys.exit()
    elif answer == "report":
        for x in resources:
            print(f"{x.title()}: {resources[x]}")
    else:
        print("Incorrect choice.")
