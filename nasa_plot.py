import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Style from your notes (Screenshot 1)
plt.style.use('fivethirtyeight')


def animate(i):
    # Part 1: Read the CSV being written by the generator
    data = pd.read_csv('data.csv')

    # Part 2: Use .tail(50) to only show the last 50 points.
    # This prevents the "memory crash" and makes the graph move/scroll.
    recent_data = data.tail(50)

    x = recent_data['x_value']
    y = recent_data['altitude']

    # Part 3: Clear and Redraw (Screenshot 1)
    plt.cla()  # Clear current axes so old lines don't stack

    # AREA TO ALTER: Change labels or colors based on quiz rules
    plt.plot(x, y, label='ISS Altitude (km)')

    plt.legend(loc='upper left')
    plt.tight_layout()


# Part 4: The Animation Timer (Screenshot 1)
# interval=1000 means it refreshes every 1 second
ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)

plt.show()