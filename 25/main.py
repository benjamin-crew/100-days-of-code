import csv
import pandas

# with open("25/weather_data.csv") as data_file:
#     data = list(csv.reader(data_file))
#     temperature = []
    
#     for line in data[1:]:
#         temperature.append(int(line[1]))


#     print(temperature)

data = pandas.read_csv("/Users/benja/Documents/Python/100-days-of-code/25/weather_data.csv")
avg_temp = 0

for temp in data["temp"]:
    avg_temp += temp

avg_temp = avg_temp / len(data["temp"])
print(avg_temp)

# or
# data["temp"].mean()