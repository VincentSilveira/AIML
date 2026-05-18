import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("Loading Housing Dataset...")


url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
data = pd.read_csv(url)

print("Dataset Loaded!\n")


print(data.head())

X = data.drop("median_house_value", axis=1)   # Factors
y = data["median_house_value"]                # Price

X = X.drop("ocean_proximity", axis=1)
X = X.fillna(X.mean())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Trained Successfully!")


predictions = model.predict(X_test)

print("\nSample Predictions:")

for i in range(3):
    print("Actual:", y_test.iloc[i],"| Predicted:", round(predictions[i], 2))

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Accuracy (R2 Score):", round(r2, 2))
print("Model Error (MSE):", round(mse, 2))


if r2 > 0.70:
    print("\nDecision: Model is GOOD for prediction.")
else:
    print("\nDecision: Model needs improvement.")

print("\nProgram Finished.")