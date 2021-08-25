# Day 21 - Intermediate - Build the Snake Game Part 2: Inheritance & List Slicing

### Class Inheritence

Imagine having a 'chef' model.
A Chef class has methods for baking, stirring, measuring.

Now imagine you need a pastry chef. You can inherit from 'chef', and then add a couple extra methods.

This saves you typing out all the methods and attributes a second time for a new class.

    class PastryChef(Chef):
        def __init__(self):
            super().__init__()

In the example above, Chef is the super class, and the PastryChef is inheriting the 
attributes and methods of the super class.

You can also inherit and modify things from super classes. For instance:

    class Animal:
        def __init__(self):
            self.num_eyes(2)
        
        def breathe(self):
            print("Inhale, exhale.")
    
    class Fish(Animal):
        def __init__(self):
            super().__init__()
        
        def breathe(self):
            super().breathe()
            print("Doing this underwater.")
        