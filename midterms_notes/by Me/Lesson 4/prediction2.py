import numpy as np
import matplotlib.pyplot as plt # 1. ADD THIS IMPORT
from sklearn.linear_model import LinearRegression

# 1. Manual Data (Years vs Salary)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([25000, 32000, 41000, 50000, 58000])

# 2. Fit the model
model = LinearRegression().fit(X, y)

# 3. Predict for 10 years
ans = model.predict([[10]])
print(f"Prediction for year 10: {ans[0]}")

# --- 4. ADD THESE PLOTTING LINES ---
plt.scatter(X, y, color='blue')       # Draws the actual data points
plt.plot(X, model.predict(X), color='red') # Draws the regression line
plt.title('Salary Prediction Model')
plt.xlabel('Years')
plt.ylabel('Salary')
plt.show()                            # THIS IS THE KEY: It opens the window!
# -----------------------------------