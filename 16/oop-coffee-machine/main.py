from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

# Variables
coffees_ordered = 0
is_on = True

# Ask if user wants coffee
while is_on is True:
    if coffees_ordered == 0:
        answer = input("Would you like a coffee? Yes/no: ").lower()
    elif coffees_ordered > 0:
        answer = input("Would you like another coffee? Yes/no: ").lower()

    if answer == "yes":

        # Display menu
        print_menu = menu.get_items().replace("/", "\n")
        print(f"Our available coffees are:\n{print_menu.title()}")

        # Get users choice
        choice = input("What would you like to drink to order?: ").lower()

        # Check resources
        choice_menuitem = menu.find_drink(choice)

        if choice_menuitem != None:

            enough_resources = coffee_maker.is_resource_sufficient(choice_menuitem)
            if enough_resources == True:

                # Process coins
                payment = money_machine.make_payment(choice_menuitem.cost)

                if payment == True:
                    coffees_ordered += 1
    elif answer == "no":
        is_on = False
    elif answer == "off":
        print("Switching the machine off")
        is_on = False
    elif answer == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        print("Incorrect choice.")
