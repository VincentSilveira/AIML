from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier


X, y = load_iris(return_X_y=True)


model = KNeighborsClassifier()


scores = cross_val_score(model, X, y, cv=5)
print("Accuracy:", scores.mean())


grid = GridSearchCV(model, {'n_neighbors': [3,5,7]}, cv=5)
grid.fit(X, y)

print("Best k:", grid.best_params_)
print("Best Accuracy:", grid.best_score_)