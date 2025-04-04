import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample data: Study hours vs. Pass/Fail (1=Pass, 0=Fail)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

# Predict if a student studying 3.5 hours will pass
prediction = model.predict([[3.5]])
print("Pass Prediction:", prediction[0])  # Output: 1 (Pass)
