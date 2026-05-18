import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


X = np.array([500, 750, 1000, 1250, 1500, 1750, 2000]).reshape(-1, 1)
y = np.array([50, 75, 100, 130, 150, 180, 210])   # Price in lakhs


model = LinearRegression()


model.fit(X, y)

predicted_price = model.predict([[1600]])


print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)
print("Predicted price for 1600 sq.ft:", predicted_price[0], "lakhs")


plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("House Size (sq.ft)")
plt.ylabel("House Price (lakhs)")
plt.title("Linear Regression - House Price Prediction")
plt.show()
