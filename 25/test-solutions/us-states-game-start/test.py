import pandas

data = pandas.read_csv("/Users/benja/Downloads/test/us-states-game-start/50_states.csv")
answer_state = "Utah"

attempt = data[data["state"] == answer_state]

x = attempt["x"]
y = attempt["y"]

print(x)