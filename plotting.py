from matplotlib import pyplot as plt
import random
from itertools import count
from matplotlib.animation import FuncAnimation
import pandas as pd

plt.style.use('fivethirtyeight')
x_vals = []
y_vals = []
index = count()
def animate(i):
    df = pd.read_csv('data.csv')
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))
    plt.cla()
    plt.scatter(x,y1, label = "Chanel 1")
    plt.scatter(x, y2, label="Chanel 2")
    plt.legend()
    plt.tight_layout()

    ani = FuncAnimation(plt.gcf(), animate, interbal = 1000, cache_frame_data=False)