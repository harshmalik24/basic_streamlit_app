import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

#reading the dataset
dataset = pd.read_csv(r"C:\Users\harsh\Desktop\Intern\project2\pages\Mall_Customers.csv")
X=dataset.iloc[:, :].values
print(X)

#creating a dendrogram to determine the number of clusters (here we can choose either 3 or 5 clusters)
dendrogram = sch.dendrogram(sch.linkage(X,method = "ward"))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Eucledian Distance")
plt.show()

st.title("Hierarchical clustering")
st.header("Dataset (Mall Customers)")
st.dataframe(dataset)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.header("Dendrogram")
st.pyplot(plt.show())

#performing clustering
clustering = AgglomerativeClustering(n_clusters = 5)
y_hc=clustering.fit_predict(X)

#Plotting the result of clustering
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], c='red', label='Cluster1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], c='blue', label='Cluster2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], c='green', label='Cluster3')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], c='orange', label='Cluster4')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], c='brown', label='Cluster5')
plt.title('Cluster of Customers')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()

st.set_option('deprecation.showPyplotGlobalUse', False)
st.header("Clusters of customers")
st.subheader("Based on their income and spending score")
st.pyplot(plt.show())



