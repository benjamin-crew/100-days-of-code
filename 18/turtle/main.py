from turtle import Turtle, Screen
from random import choice

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("green")

colorlist = [
    "cyan",
    "black",
    "aquamarine",
    "brown2",
    "DarkCyan",
    "DarkGreen",
    "DarkSlateBlue",
]

directions = [
    "left",
    "right",
]

# Draw a square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# Draw a dotted line
# for _ in range(14):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# Draw shapes of increasing sides

# def draw_shape(shape_angle):

#     angle = 360 / number_of_sides

#     for turn in range(number_of_sides):
#         turtle.forward(100)
#         turtle.right(angle)


# for number_of_sides in range(3, 10):

#     randomcolor = choice(colorlist)
#     turtle.pencolor(randomcolor)

#     draw_shape(number_of_sides)

# Draw a random walk

for _ in range(200):
    random_direction = choice(directions)

    if random_direction == "left":
        turtle.left(90)
        turtle.forward(100)
    else:
        turtle.right(90)
        turtle.forward(100)


screen.exitonclick()