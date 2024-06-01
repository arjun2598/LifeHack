# LifeHack Solution 

  Team: AAGJ  
  Theme 3: Safeguarding Public Security  
  Subtheme 1: Strengthening Domestic Security

## Solution Overview

<p>
  Given a dataset of local crimes, clusters will be generated following K-Means Clustering and corresponds to crime hotspots. Then, using openrouteservice API, routes from each police division to its nearest clusters are generated, by comparing the coordinates of each division with the coordinates of each cluster's centroid.
</p>

## How to Use
<p>
  Our project is a web application where each police division is marked out on the homepage. Clicking on a marker brings you to the respective route for that division. For our use, we created a sample data set of 250 coordinates within Singapore and generated 20 clusters from that data set, but due to some coordinates being invalid (ie. being unreachable by car, in a body of water, etc.), we cleaned the data to 15 clusters. Hence, for each of the 7 police divisions currently present domestically, we generated a route to their nearest 3 clusters. Each route is generated as a html file, which displays the routes on our web application. 
</p>

