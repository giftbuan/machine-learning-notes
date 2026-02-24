import matplotlib.pyplot as plt
#These lists act as your "date" instead of a csv
ages_x = [25, 36, 27, 28, 29, 30, 31, 32, 33, 34, 35]
salaries_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, salaries_y, label='All Devs')
plt. title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salaries (USD)')
plt.legend()
plt.show()