from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


iris = load_iris()
X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')


svm_model.fit(X_train, y_train)


y_pred = svm_model.predict(X_test)


print("SVM Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


"""
Support Vector Machine (SVM) is a supervised learning algorithm used for classification and regression tasks.
SVM works by finding the optimal hyperplane that separates data into different classes.
The algorithm maximizes the margin between the decision boundary and the nearest data points called support vectors.
SVM can handle:
Linear classification
Nonlinear classification
Nonlinear classification is achieved using the Kernel Trick:
Linear Kernel
Polynomial Kernel
RBF Kernel
SVM performs effectively in:
Face recognition
Spam filtering
Text classification
Bioinformatics
Evaluation metrics:
Accuracy
Precision
Recall
F1-score
Advantages:
Effective in high-dimensional spaces
Good generalization
Limitations:
Computationally expensive
Difficult parameter tuning for large datasets
"""
