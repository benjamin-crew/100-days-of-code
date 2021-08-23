# Day 18 - Intermediate - Turtle & the Graphical User Interface (GUI)

Modules are essentially seperate files for functions that you can import.

### Import

    import random #import full module
    from random import random #for specific function, comma seperate for multiple functions.


### Creating a module

Just save your function as a py file

    def make_pizza(size, *toppings):
        #Summarise the pizza we are about to make.
        print(f"Making a {size}-inch pizza with the following toppings:")
        for topping in toppings:
            print(f"- {topping}")

### Import function or module as alias

    from pizza import make_pizza as mp
    import pizza as p