from math import ceil


def area_calc(wall_height, wall_width, coverage):
    return(ceil((wall_height * wall_width) / coverage))


coverage = int(input("How many square meters of wall does one can cover: "))
wall_height = int(input("What is the height of your wall: "))
wall_width = int(input("What is the width of your wall: "))

print(f"You require: {area_calc(wall_height, wall_width, coverage)} cans.")
