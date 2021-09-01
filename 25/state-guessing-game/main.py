import turtle
import pandas
import sys
from states_class import StateClass


data = pandas.read_csv("25/state-guessing-game/50_states.csv")
image = "25/state-guessing-game/blank_states_img.gif"

screen = turtle.Screen()

score = 0
all_states = data.state.tolist()
guessed_states = []
missing_states = []

screen.title("US States Quiz")
screen.addshape(image)
turtle.shape(image)

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct (q to quit).", prompt="Enter the name of a State.").title()

    if answer_state == "Q":
        break

    for state in data["state"]:
        if state == answer_state:
            x = int(data.x[data.state == state])
            y = int(data.y[data.state == state])
            guessed_states.append(answer_state)
            state = StateClass(answer_state, x, y)
            score += 1


if score == 50:
    turtle.write(f"Congratulations, you win!!!", align="center", font=("Arial", 48, "normal"))
else:
    missing_states = [state for state in all_states if state not in guessed_states]

    missing_states_df = pandas.DataFrame(missing_states)
    missing_states_df.to_csv("25/missing_states.csv")
    
screen.exitonclick()