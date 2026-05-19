
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


"""
K-Means is an unsupervised machine learning algorithm used for clustering similar data points into groups.
The algorithm partitions data into K clusters where K is predefined by the user.
Each cluster is represented by a centroid.
Working steps:
Choose K clusters
Initialize random centroids
Assign points to nearest centroid
Update centroids
Repeat until convergence
Distance is calculated using Euclidean Distance:
d=
(x
2
	​

−x
1
	​

)
2
+(y
2
	​

−y
1
	​

)
2
	​

-10
-8
-6
-4
-2
2
4
6
8
10
-10
-5
5
10
A(6.0, 6.0)
B(-6.0, -6.0)
d = 16.97
Delta x = 12
Delta y = 12
K-Means is commonly used in:
Customer segmentation
Image compression
Recommendation systems
Market analysis
Advantages:
Fast and scalable
Easy implementation
Limitations:
Sensitive to outliers
Requires predefined K
Assumes spherical clusters
"""
