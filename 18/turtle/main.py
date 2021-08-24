from turtle import Turtle, Screen
from random import choice, randint

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("green")
screen.colormode(255)

colorlist = [
    "cyan",
    "black",
    "aquamarine",
    "brown2",
    "DarkCyan",
    "DarkGreen",
    "DarkSlateBlue",
]

directions = [0, 90, 180, 270]

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

# turtle.pensize(15)
# turtle.speed(9)
# for _ in range(200):
    
#     random_direction = choice(directions)
    
#     turtle.pencolor((randint(0,255), randint(0,255), randint(0,255)))
#     turtle.setheading(random_direction)
#     turtle.forward(20)

# Draw a circle
turtle.speed(0)
heading = 0
tilt = 5
circles = 360 / tilt
for _ in range(0,int(circles)):

    turtle.pencolor((randint(0,255), randint(0,255), randint(0,255)))
    turtle.setheading(heading)
    turtle.circle(100, steps=100)
    heading += 5

screen.exitonclick()