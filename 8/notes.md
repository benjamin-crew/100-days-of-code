### Function Parameters & Caesar Cipher

## Functions
All my functions notes are here: https://www.notion.so/2ade684e759c44aebfe0344fc402c161?v=967010a9f1ac4418ad7c9bbb1eb6734e&p=2e30b7552fff4591b123db7fd8f85e65

# Positional Arguments
    def greet_user(first_name, surname): 
        print(f"Hi there, {first_name} {surname}!") 
        print("Welcome aboard") 

    print("Start") 

    # These are positional arguments. The position of the arguments passed into the 'greet user' function 
    # matters. So whatever is first will be the first argument, in this case first_name, and whatever 
    # is second will be the surname. 

    greet_user("John", "Smith") 
    print("Finish")

# Keyword Arguments
    def greet_user(first_name, surname): 
    print(f"Hi there, {first_name} {surname}!") 
    print("Welcome aboard") 

    print("Start") 

    # This script uses keyword arguments, which means the position of the arguments below 
    # doesn't matter,as we have mapped the string to the argument manually. 

    greet_user(surname="Smith", first_name="John") 

    print("Finish")

Use positional where possible. Keyword arguments should be used to improve readability. If using both positional and keyword arguments, keyword arguments have to come after positional arguments.

# Default Value
You can use a default value as a parameter.

    def greet_user(first_name, surname="Smith"): 
        print(f"Hi there, {first_name} {surname}!") 
        print("Welcome aboard") 

    greet_user("John")  

The surname is set to a default of Smith, so the user doesn't have to type this. They can just type their first name in the greet_user() function call.
When using default values, make sure to put them after all positional values, so Python can continue to interpret the positionals correctly.

# Return Value
    def square(number):
	    return number * number

    print(square(3))

This prints the number in brackets squared, i.e. 9. The print statement knows the answer because the square function returns it.

# Optional Arguments
The following function has three arguments. Middle name might not always be necessary:

    def get_formatted_name(first_name, middle_name, last_name):
        #Return a full name, neatly formatted.
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()

    person = get_formatted_name('ben', 'john', 'crew')
    print(person)

To make middle_name optional, we set it to a blank string and move it to the end of the arguments. Then we can do an if statement that says, if middle_name is populated, use it. If not, dont. Example:

    def get_formatted_name(first_name, last_name, middle_name=""):
        #Return a full name, neatly formatted.
        if middle_name:
            full_name = f"{first_name} {middle_name} {last_name}"
        else:
            full_name = f"{first_name} {last_name}"

        return full_name.title()

    person = get_formatted_name('ben', 'crew')
    print(person)

middle_name is shifted to the end to make sure positional arguments apply correctly.