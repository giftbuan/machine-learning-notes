import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


def animate(i):
    # Part 1: Read the CSV being written by the generator
    data = pd.read_csv('../data.csv')
    recent_data = data.tail(30)

    x = recent_data['x_value']
    y = recent_data['total_1']
    plt.cla()  # Clear current axes so old lines don't stack

    plt.xlim(0, 100)
    plt.ylim(800, 1200)

    plt.scatter(x,y, c = 'red', label='Sensor Right')
    plt.scatter(100 -x, recent_data['total_2'], c='blue', label='Sensor Left')

    plt.legend(loc='upper left')
    plt.tight_layout()

#The Animation Timer
ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)
plt.show()