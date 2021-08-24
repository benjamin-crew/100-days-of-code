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

### Tuple
A tuple is just a list but immutable. It cannot be changed. You declare it the same way but use curly brackets instead of square.

    dimensions = (200, 50)
    print(dimensions[0])

It's actually the comma that defines a tuple, not the parenthesis. To declare a single element tuple, you would have to make sure to put the trailing comma:

    dimension = (200,)


## Turtle

In the turtle folder is a script with a bunch of different things you can do
within the turtle GUI tool.

### Random RGB Generator

Creating a random RGB color in a tuple:

    turtle.pencolor((randint(0,255), randint(0,255), randint(0,255)))