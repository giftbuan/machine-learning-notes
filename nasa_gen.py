import csv
import random
import time

# Variables for the data columns (Screenshot 2)
x_value = 0
altitude = 420

# fieldnames must match the keys in the 'info' dictionary below
fieldnames = ['x_value', 'altitude']

# Part 1: Create the file and write the header once (Screenshot 2)
with open('data.csv', 'w') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()

while True:
    # Part 2: Open file in 'a' (append) mode to add new data rows
    with open('data.csv', 'a') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # info holds the actual data values (Screenshot 2)
        info = {
            'x_value': x_value,
            'altitude': altitude
        }

        csvwriter.writerow(info)
        print(x_value, altitude)  # Helpful for checking progress

        x_value += 1

        # AREA TO ALTER: This simulates the data changing.
        # If the quiz asks for a specific range, change these numbers.
        altitude = altitude + random.uniform(-0.5, 0.5)

    # IMPORTANT: Matches the refresh rate of the plot (Screenshot 2)
    time.sleep(1)