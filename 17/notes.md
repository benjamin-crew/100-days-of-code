### The Quiz Project & the Benefits of OOP

## Class

A class can be used as a blueprint to model real-world things, situations or data.
You can create an object from a class and that will inherit all the classes properties.
This is called an instance, and the process of creating an instance is called Instantiation.

Example:

    class Dog:
    """A Simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialise name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")


    my_dog = Dog('Boris', 6)
    your_dog= Dog("Winston", 3)

    print(f"My dog's name is {my_dog.name}.")
    print(f"My dog is {my_dog.age} years old.")

    print(f"Your dog's name is {your_dog.name}.")
    print(f"Your dog is {your_dog.age} years old.")


    my_dog.sit()
    my_dog.roll_over()

# Class Declaration

Use PascalCase:

    class Car:

# Create Object

    bmw = Car()

# Create a class attribute

An attribute is just a variable that is associated to an object.
Use . notation after object:

    bmw.speed = 160

Rather than setting these attributes per object, you would use a constructor

# Constructor

A constructor tells the class what properties to give an object when it is being constructed, or initialised.
To do this, you use the __init__ function:

    class User:

        def __init__(self):

init is called every time an object is created from the class.

    import random


    class User:
        def __init__(self, name, num):
            self.name = name
            self.favourite = num

    num = 10

    for i in range(0, num):
        i = str(i)
        user = "user" + i
        favourite_number = random.randint(0, 50)
        user = User(user, favourite_number)
        print(f" {user.name} created. He has a favourite number of {user.favourite}")