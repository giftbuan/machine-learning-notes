import csv
import random
import time

from data_gen import total_1

# Variables for the data columns
x_value = 0
total_1 = 1000
total_2 = 1000

# fieldnames must match the keys in the 'info' dictionary below
fieldnames = ['x_value', 'total_1', 'total_2']

# Create file and write the HEADER
with open('../data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()

while True:
    # Open file in 'a' (append) mode to add new data rows
    with open('../data.csv', 'a') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # info holds the actual data values
        info = {
            'x_value': x_value,
            'total_1': total_1,
            'total_2': total_2,
        }
        csvwriter.writerow(info)
       # print(x_value, altitude)  # Helpful for checking progress
        x_value += 1
        if x_value > 100:
            x_value = 0
            total_1 = total_1 + random.randint(-10, 10)
            total_2 = total_2 + random.radint(-10, 10)

    #Matches the refresh rate of the plot
    time.sleep(0.1)