import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)

model = KMeans(n_clusters=2)
model.fit(X)

labels = model.labels_
centroids = model.cluster_centers_

plt.title('K-Means')
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='X', s=200)
plt.show()