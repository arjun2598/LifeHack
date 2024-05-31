# LifeHack Solution 

  Team: AAGJ  
  Theme 3: Safeguarding Public Security  
  Subtheme 1: Strengthening Domestic Security

  Solution Overview: Given a dataset of local crimes, we will generate clusters that correspond to crime hotspots. Then, using the openrouteservice API, we generate routes from each police division to its nearest k clusters using the coordinates of each division, and the coordinates of the centres of each cluster. Finally, we created a web application where each police division is marked out and clicking on each marker brings you to the specific route for that division. In our use, we created a sample data set of 250 coordinates within Singapore and generated 20 clusters from that data set, but due to some coordinates being unreachable, we cleaned the data to 15 clusters. Hence, for the 7 divisions currently present locally, we generated a route to the nearest 3 clusters (k = 3), and each route is generated as an html file, which we used to display the routes on our web application.
