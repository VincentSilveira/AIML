
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])  # 0 = Fail, 1 = Pass


model = LogisticRegression()

model.fit(X, y)

hours = 5
prediction = model.predict([[hours]])
probability = model.predict_proba([[hours]])


print("Prediction for", hours, "hours:", "Pass" if prediction[0] == 1 else "Fail")
print("Probability:", probability)

plt.scatter(X, y)
plt.plot(X, model.predict_proba(X)[:, 1])
plt.xlabel("Study Hours")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression - Student Result Prediction")
plt.show()
