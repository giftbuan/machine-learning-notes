import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Load the data
df = pd.read_csv('prediction.csv')

df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df = df.dropna()
# ---------------------------

# 2. Select the data
X = df[['YearsExperience']].values
y = df['Salary'].values

model = LinearRegression()
model.fit(X, y)

# 3. Create and Train the model
model = LinearRegression()
model.fit(X, y)

# 4. Predict salary for someone with 10 years of experience
prediction = model.predict([[10]])
print(f"Predicted Salary for 10 years: {prediction[0]:.2f}")

# 5. Visualize (Optional but great for extra points)
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Prediction Line')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary (PHP)')
plt.legend()
plt.show()