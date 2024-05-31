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
    centroids = kmeans.cluster_centers_
    df = pd.DataFrame(centroids)
    df.to_csv('./clustering/clusters.csv', index=False)
    
    

data = read_file("./clustering/random_coordinates_singapore.csv") 
k_means_clustering(data, 20)

