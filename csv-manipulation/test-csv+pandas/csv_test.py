import csv

with open('weather_data.csv') as data:
    contents = csv.reader(data)
    # extract temps from the file
    temperatures = []
    for row in contents:
        for word in row:
            if word.isdigit():
                temperatures.append(int(row[1]))

    print(temperatures)

average = sum(temperatures) / len(temperatures)
print(f'{average:.2f}')
