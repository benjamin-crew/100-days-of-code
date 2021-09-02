### Day 27 - Tkinter, *args, **kwargs and Creating GUI Programs

## Tkinter
Tkinter is installed by default.
To use it, create a window and a mainloop to display the window. The main loop must be at the end of your code.

    window = tkinter.Tk()

    window.mainloop()

Tkiner uses a method called packer, which manages the relative positioning of widgets in their containers.
Documentation here: https://docs.python.org/3/library/tkinter.html#the-packer

    # Create Label
    my_label = tkinter.Label(text="I am a label.", font=("Arial", 24, "bold"))
    # Display Label
    my_label.pack(side="top")

## Default values
Sometimes, a function will have arguments that have default values, i.e:
    
    def my_function(arg, a=2, b=3, c=4):

In the example above, I need to specify an 'arg', but I don't have to specify a, b or c, as they have default values. I can however specify any of them if I want:

    my_function(ben, b=14)
    my_function(ben, 14)
    my_function(ben, 14, 16)


## *args
*args are variable number arguments, or unlimited arguments.

    def add(*args):
        for n in args:
            print(n)
    
    add(2, 4, 6 ,8)

    def add(*args):

    # function to add all args
    def add(*args):

        num = 0
        for n in args:
            num += n
        return(num)

        print(add(2, 4, 6 ,8))

## **kwargs
**kwargs is a way of specifying as many keyword arguments as you like, but giving them default value also.
The kwargs are stored as a dictionary.

    def calculate(n, **kwargs):

    print(kwargs)
    # for key, value in kwargs.items():
        # print(key)
        # print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

    calculate(2, add=3, multiply=5)