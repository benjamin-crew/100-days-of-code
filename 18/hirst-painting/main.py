# import colorgram

# colors = colorgram.extract('hirst.jpeg', 6)
# colors_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     colors_list.append(rgb_tuple)

from turtle import Turtle, Screen
from random import randint

color_list = [(229, 228, 226), (225, 223, 225), (199, 175, 117), (212, 222, 215), (125, 36, 24), (223, 224, 228)]
turtle = Turtle()
screen = Screen()

screen.screensize(500, 500)
screen.colormode(255)

y = -250

for _ in range(0, 10):
    x = -250

    for _ in range(0,10):

        random_color = color_list[randint(0, len(color_list) - 1)]

        turtle.penup()
        turtle.setpos(x, y)

        turtle.pendown()
        turtle.dot(20, (random_color))
        x += 50

    y += 50


screen.exitonclick()
