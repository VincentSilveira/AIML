from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

# X is the area
X = np.array([100, 200, 500, 1000, 500, 320, 640, 700]).reshape(-1, 1)
y = np.array([1100, 2400, 6200, 13000, 7300, 4000, 7200, 9000])


model = LinearRegression()
model.fit(X, y)

print(model.coef_)
print(model.intercept_)

pred = model.predict(np.array([50, 730, 1100]).reshape(-1,1))
print(pred)
