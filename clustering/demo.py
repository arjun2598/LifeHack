from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

# function to read file. 
def read_file(file):
    df = pd.read_csv(file)
    df1 = df[["Longitude", "Latitude"]]
    return df1.values.tolist()



def k_means_clustering(data, num_clusters):
    """
    Performs K-means clustering on the provided data.
    
    Parameters:
    data (array-like or matrix): The input data to cluster.
    num_clusters (int): The number of clusters to form.
    
    Returns:
    labels (array): The labels of the clusters.
    centroids (array): The coordinates of the cluster centers.
    """
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans.fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    return labels, centroids

# test = [[103.8607, 1.2834], [103.8159, 1.3138], [103.8303, 1.2494], [103.7075, 1.3192], [103.9915, 1.3644]]
data = read_file("./random_coordinates_singapore.csv") 
print(k_means_clustering(data, 20)[1])

