import turtle
import pandas
import sys



data = pandas.read_csv("/Users/benja/Downloads/test/us-states-game-start/50_states.csv")
screen = turtle.Screen()
image = "/Users/benja/Downloads/test/us-states-game-start/blank_states_img.gif"
score = 0
guessed_states = []

screen.title("US States Quiz")
screen.addshape(image)
turtle.shape(image)

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Enter the name of a State.")

    if answer_state == "q":
        sys.exit()

    for states in data:
        if states["state"] == answer_state:
            if answer_state not in guessed_states:
                score += 1
                guessed_states.append(answer_state)
                correct_state = data[data["state"] == answer_state]
                x = correct_state["x"]
                y = correct_state["y"]




screen.exitonclick()