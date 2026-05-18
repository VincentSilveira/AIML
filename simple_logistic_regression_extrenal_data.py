
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

print("Loading Dataset...")


data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)


df["Target"] = data.target

print("Dataset Loaded!\n")


print(df.head())




X = df.drop("Target", axis=1)   # Features
y = df["Target"]                # Output (0 = Malignant, 1 = Benign)




X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

predictions = model.predict(X_test)

print("\nSample Predictions:")

for i in range(5):
    print("Actual:", y_test.iloc[i],
          "| Predicted:", predictions[i])



accuracy = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nConfusion Matrix:")
print(cm)



