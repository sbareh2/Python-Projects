import pandas


#data = pandas.read_csv('weather_data.csv')

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].tolist()
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
# # Get data in columns
# print(data['condition'])
# print(data.condition)

# # Get data in row
# print(data[data.day == 'Monday'])
#
# # print row with max temp
# print(data[data.temp == data['temp'].max()])

# monday = data[data.day == 'Monday']
# print(monday.condition)
#
# # convert monday temp to F
# f_temp = (monday.temp * (9/5)) + 32
# print(f_temp)

# create a dataframe from scratch
data_dict = {'students': ['Amy', 'James', 'Angela'], 'scores': [76, 56, 65]}
data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')