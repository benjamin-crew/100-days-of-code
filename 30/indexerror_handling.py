#--------ORIGINAL---------#

# fruits = ["Apple", "Pear", "Orange"]

# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")


# make_pie(4)



#----------FIXED--------------
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as index_error:
        print(f"{index_error} is not valid input.")
    else:
        print(fruit + " pie")


make_pie(4)
