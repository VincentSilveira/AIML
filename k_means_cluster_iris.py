
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


iris = load_iris()
X = iris.data[:, :2]   # Take only 2 features for easy visualization


kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)


labels = kmeans.labels_
centers = kmeans.cluster_centers_


plt.scatter(X[:, 0], X[:, 1], c=labels)
# Plot cluster centers
plt.scatter(centers[:, 0], centers[:, 1], marker='X', s=200)


plt.xlabel("Feature 1 (Sepal Length)")
plt.ylabel("Feature 2 (Sepal Width)")
plt.title("K-Means Clustering using Iris Dataset")


plt.show()