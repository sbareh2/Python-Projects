import pandas

# create table from census with total number of each primary fur color
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_count)
print(red_count)
print(black_count)

data_dict = {'Fur color': ['Gray', 'Cinnamon', 'Black'],
             'Count': [grey_count, red_count, black_count]
             }

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
