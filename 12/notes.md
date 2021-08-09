### Scope & Number Guessing Game

## Local and Global Scope
Variables within functions have Local Scope. These variables can only be accessed from within the function.
Variables outside of functions, in the top-level of the file, are in the Global Scope. These can be referenced in functions and outside of functions.

## Block Scope
Block scope does not exit in Python. if/else blocks don't create they're only local scope, they just inherit the local scope of their function.

## Global Variables
    
    enemies = 1

    def increase_enemies():
        enemies += 1
        print(enemies)

In the code block above, enemies within the function hasn't actually been created. I'm trying to reference the global variable, but the function is operating in it's own local scope and therefore isn't aware of the enemies variable. To get around this, I can prefix 'enemies' with 'global', so that it knows to look for the variable in the global scope.
    
    enemies = 1

    def increase_enemies():
        global enemies += 1
        print(enemies)

## Constants
If you want to store a value that should never be changed, i.e. the value of pi, they you can use a constant.
A constant is just a variable but you use all caps for the naming convention.

    def change_variable(VAR):
    VAR += 1
    return VAR

    VAR = 1
    print(VAR)
    change_variable(VAR)
    print(VAR)
    VAR += 1

    print(VAR)

Just be careful with constants as it is essentially just a naming convention. You could still overwrite the value if you're not careful.