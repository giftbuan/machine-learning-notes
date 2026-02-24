import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Load the data from the CSV file
df = pd.read_csv('travel_data.csv')

# 2. Prepare the data
# X (Features) must be 2D; y (Target) is 1D
X = df[['snacks_shared']].values
y = df['kisses_received'].values

# 3. Create and train the model
model = LinearRegression()
model.fit(X, y)

# 4. Make a prediction
# If I share 15 snacks in Vietnam, how many kisses?
future_snacks = [[15]]
predicted_kisses = model.predict(future_snacks)

# 5. Visual Check (Optional but helpful for exams)
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title("Relationship: Snacks Shared vs Kisses")
plt.xlabel("Snacks Shared")
plt.ylabel("Kisses Received")
plt.legend()
plt.show()
print(f"Prediction for 15 snacks: {predicted_kisses[0]:.2f}")