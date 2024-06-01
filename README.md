# LifeHack Solution 

  Team: AAGJ  
  Theme 3: Safeguarding Public Security  
  Subtheme 1: Strengthening Domestic Security

## Solution Overview

Given a dataset of local crimes, clusters will be generated following K-Means Clustering and corresponds to crime hotspots. Then, using the openrouteservice API, routes from each police division to its nearest clusters are generated, comparing the coordinates of each division with the coordinates of each cluster's centroid. Our project is a web application where each police division is marked out on the homepage. Clicking on a marker brings you to the respective route for that division. In our use, we created a sample data set of 250 coordinates within Singapore and generated 20 clusters from that data set, but due to some coordinates being unreachable, we cleaned the data to 15 clusters. Hence, for the 7 divisions currently present locally, we generated a route to the nearest 3 clusters (k = 3), and each route is generated as an html file, which we used to display the routes on our web application.

## How to Run 
