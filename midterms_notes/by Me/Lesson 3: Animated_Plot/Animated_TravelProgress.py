import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#df = pd.read_csv('name-of-csv.csv')
# 1. DATA: Always define these first!
countries = ['Vietnam (Hanoi)', 'Laos', 'Cambodia', 'Vietnam (HCM)']
food = [3000, 10000, 7500, 7500]

# 2. SETUP: Create the figure and axis
fig, ax = plt.subplots()
x_data, y_data = [], []
# This 'ln' (line) is what will be updated in the animation
ln, = plt.plot([], [], 'go', animated=True, lw=2)

# 3. INIT: Sets the "empty" state of the graph
def init():
    ax.set_xlim(-0.5, 3.5) # Based on 4 countries (index 0-3)
    ax.set_ylim(0, 11000)  # Based on your max budget of 10,000
    ax.set_title("Travel Spending Progress")
    ax.set_ylabel("Cost (PHP)")
    return ln,

# 4. UPDATE: This runs for every 'frame' (country)
def update(frame):
    x_data.append(frame)
    y_data.append(food[frame])
    ln.set_data(x_data, y_data)
    # We can also update the x-axis labels dynamically
    plt.xticks(range(len(countries)), countries, rotation=15)
    return ln,

# 5. ANIMATION: 'frames' is 4 (range(len(countries)))
# 'interval=1000' means it moves to the next country every 1 second
ani = FuncAnimation(fig, update, frames=range(len(countries)),
                    init_func=init, blit=True, interval=1000, repeat=False)

plt.tight_layout()
plt.show()