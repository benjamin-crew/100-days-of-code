import csv
import pandas

# with open("25/weather_data.csv") as data_file:
#     data = list(csv.reader(data_file))
#     temperature = []
    
#     for line in data[1:]:
#         temperature.append(int(line[1]))


#     print(temperature)

data = pandas.read_csv("/home/benja/Documents/Development/Python/100-days-of-code/25/weather_data.csv")
# avg_temp = 0

# for temp in data["temp"]:
#     avg_temp += temp

# avg_temp = avg_temp / len(data["temp"])
# print(avg_temp)

# # or
# print(data["temp"].mean())


# get row that is max temp
# print(data[data.temp == data.temp.max()])

# convert mondays temp to fahrenheit

# monday = data[data.day == "Monday"]
# temp_fahrenheit = int(monday.temp) * 9/5 + 32
# print(temp_fahrenheit)

# Create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("test.csv")