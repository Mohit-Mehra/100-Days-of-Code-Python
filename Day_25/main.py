# with open("Day_25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open("Day_25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)

import pandas

# data = pandas.read_csv("Day_25/weather_data.csv")
# print(type(data))
# print(data["temp"])
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)


# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.day == "Monday"])

# create dataframe
# data_dict = {"students": ["Blazorus", "Goku", "Naruto"], "strength": [76, 100, 80]}
# data = pandas.DataFrame(data_dict)
# data.to_csv("Day_25/new_data.csv")


data = pandas.read_csv("Day_25/2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count],
}
df = pandas.DataFrame(data_dict)
df.to_csv("Day_25/Squirrel_Count.csv")
