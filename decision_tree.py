from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


dt_model = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=4,
    random_state=42
)


dt_model.fit(X_train, y_train)


y_pred = dt_model.predict(X_test)


print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

"""

Decision Tree is a supervised learning algorithm used for classification and regression tasks.
It represents decisions using a tree-like structure consisting of:
Root Node
Decision Nodes
Branches
Leaf Nodes
The algorithm recursively splits data based on feature conditions.
Important splitting measures:
Entropy
Information Gain
Gini Index
Entropy formula:

Entropy=−∑p
i
	​

log
2
	​

(p
i
	​

)

Gini Index formula:

Gini=1−∑p
i
2
	​


Decision Trees are used in:
Loan approval systems
Medical diagnosis
Fraud detection
Advantages:
Easy interpretation
Handles categorical and numerical data
Limitations:
Overfitting
Sensitive to small data changes
"""
