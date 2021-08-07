def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return(formated_f_name + " " + formated_l_name)


first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

print(format_name(first_name, last_name))
