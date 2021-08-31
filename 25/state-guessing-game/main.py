import turtle
import pandas
import sys
from states_class import StateClass


data = pandas.read_csv("/home/benja/Documents/Development/Python/100-days-of-code/25/test-solutions/us-states-game-start/50_states.csv")
image = "/home/benja/Documents/Development/Python/100-days-of-code/25/test-solutions/us-states-game-start/blank_states_img.gif"

screen = turtle.Screen()

score = 0
guessed_states = []

screen.title("US States Quiz")
screen.addshape(image)
turtle.shape(image)

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct (q to quit).", prompt="Enter the name of a State.").lower()

    if answer_state == "q":
        sys.exit()

    for state in data["state"]:
        if state == answer_state:
            x = int(data.x[data.state == state])
            y = int(data.y[data.state == state])
            guessed_states.append(answer_state)
            state = StateClass(answer_state, x, y)
            score += 1

turtle.write(f"Congratulations, you win!!!", align="center", font=("Arial", 48, "normal"))

screen.exitonclick()