import openrouteservice as ors
import folium
import heapq
import pandas as pd

# Functions to read csv files
def read_file_with_Title(file):
    df = pd.read_csv(file)
    df1 = df[["Longitude", "Latitude","Title"]]
    return df1.values.tolist()

def read_file(file):
    df = pd.read_csv(file)
    df1 = df[["Longitude", "Latitude"]]
    return df1.values.tolist()

# Division list
divisions = read_file_with_Title("./routes/divisions.csv")

# Cluster list
clusters = read_file("./clustering/clusters.csv")

clustersPerDivision = 3 # Number of clusters for each police division to patrol

client = ors.Client(key='5b3ce3597851110001cf6248868fd2996ba346cb94ed4e3d8510544f')

# Function to calculate distance from one point to another using the route instead of physical distance
def distance(start, end):
    route = client.directions(
        coordinates=[start, end],
        profile='driving-car',
        format='geojson')
    dist = route['features'][0]['properties']['segments'][0]['distance']
    return dist

# returns array of nearest n divisions for desired n as fixed above
def extractMin(distArray):
    coords = []
    q = []

    for index in range(len(clusters)):
        heapq.heappush(q, (distArray[index], clusters[index])) # distance is the priority, cluster is the value
    for x in range(clustersPerDivision):
        _, coord = heapq.heappop(q) # outputs just cluster without distance value
        coords.append(coord)
    return coords

# Function creates map for each division 
def createMap(startingPoint, stops, division_index):

    # initialise map with coordinates of Singapore
    m = folium.Map(location=[1.290270, 103.851959], zoom_start=10, control_scale=True, tiles="cartodbpositron")

    # Marker for starting point
    folium.Marker( 
        location=list(startingPoint[::-1]),
        popup="AMK police division",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    # Markers for clusters
    for index in range(len(stops)):
        folium.Marker(
            location=list(stops[index][::-1]),
            popup=f"Cluster {index}",
            icon=folium.Icon(color="red"),
        ).add_to(m)

    vehicle_start = startingPoint
    # Algorithm requires array of vehicles to split 'jobs', but for our case just need 1 vehicle
    vehicles = [
        ors.optimization.Vehicle(id=0, profile='driving-car', start=vehicle_start, end=vehicle_start, capacity=[5])
    ]
    # Jobs are essentially the clusters we have to patrol
    jobs = [ors.optimization.Job(id=i, location=stop, amount=[1]) for i, stop in enumerate(stops)]
    optimized = client.optimization(jobs=jobs, vehicles=vehicles, geometry=True)
    line_color = 'blue'
    # Draw out route
    for route in optimized['routes']:
        folium.PolyLine(locations=[list(reversed(coord)) for coord in ors.convert.decode_polyline(route['geometry'])['coordinates']], color=line_color).add_to(m)

    output_path = f'./myproject/myapp/templates/{divisions[division_index][2]}.html' # output each map as html file
    m.save(output_path) # saves each map to appropriate location

for marker_index, start in enumerate(divisions): # iterate through divisions
    distArray = []
    startingPoint = start[:2]
    clusterCoords = [cluster[:2] for cluster in clusters]
    for coords in clusterCoords:
        dist = distance(startingPoint, coords) # calculate distance to cluster
        distArray.append(dist) 
    
    stops = extractMin(distArray)
    createMap(startingPoint, stops, marker_index)