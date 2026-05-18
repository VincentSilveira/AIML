#Demo
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


data = {
    "Income": [15,16,17,18,48,19,33,20,59,49,60,34,51,21,30],
    "Spending": [39,81,6,77,40,76,6,94,3,72,14,75,24,82,26]
}

df = pd.DataFrame(data)

# Select features
X = df[["Income", "Spending"]]

kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)


plt.scatter(df["Income"], df["Spending"], c=df["Cluster"])
plt.xlabel("Income")
plt.ylabel("Spending")
plt.title("Customer Segmentation (K-Means)")
plt.show()