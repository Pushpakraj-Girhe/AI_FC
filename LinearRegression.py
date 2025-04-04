import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data: Square footage vs. Price
X = np.array([[1000], [1500], [2000], [2500], [3000]])
y = np.array([200000, 250000, 300000, 350000, 400000])

model = LinearRegression()
model.fit(X, y)

# Predict price for a 2200 sqft house
predicted_price = model.predict([[2200]])
print("Predicted Price:", predicted_price[0])
