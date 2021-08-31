import pandas

data = pandas.read_csv("/home/benja/Documents/Development/Python/100-days-of-code/25/Squirrel_Data.csv")

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

grey_squirrels_len = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_len = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_len = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_len, red_squirrels_len, black_squirrels_len]
}


dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("squirrelcsv.csv")