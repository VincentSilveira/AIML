from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier


# Load data - iris
# Load model - KNeighboursClassifier
# get score  form cross_val_score
# Load grid - GridSearchCV
# Fit data
# Compare accuracy

X,y = load_iris(return_X_y=True)
model = KNeighborsClassifier()
scores = cross_val_score(model, X, y, cv=5)
print(scores)


grid = GridSearchCV(model, {'n_neighbors': [3,5,7]}, cv=5)
grid.fit(X, y)

print(grid.best_params_)
print(grid.best_score_)