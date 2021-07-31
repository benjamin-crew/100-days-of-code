bill = 0

small_pizza = 15
medium_pizza = 20
large_pizza = 25

small_pepperoni = 2
medium_large_pepperoni = 3
cheese = 1

size = (input("What size pizza would you like? S, M or L: ")).lower()
add_pepperoni = (input("Would you like to add pepperoni?: y/n ")).lower()
extra_cheese = (input("Extra cheese?: y/n ")).lower()

if size == "s" or size == "m" or size == "l":
    if size == "s":
        bill += small_pizza
        if add_pepperoni == "y":
            bill += small_pepperoni
        if extra_cheese == "y":
            bill += cheese

    if size == "m":
        bill += medium_pizza
        if add_pepperoni == "y":
            bill += medium_large_pepperoni
        if extra_cheese == "y":
            bill += cheese

    if size == "l":
        bill += large_pizza
        if add_pepperoni == "y":
            bill += medium_large_pepperoni
        if extra_cheese == "y":
            bill += cheese

    print(f"Your bill is: {bill}")
else:
    print("Incorrect pizza size.")