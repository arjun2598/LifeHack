import openrouteservice as ors
import folium
import heapq
import pandas as pd

# Create Division list
def read_file(file):
    df = pd.read_csv(file)
    df1 = df[["Longitude", "Latitude"]]
    return df1.values.tolist()

divisions = read_file("./routes/divisions.csv")

# Cluster list
clusters = read_file("./clustering/clusters.csv")

clustersPerDivision = 3

client = ors.Client(key='5b3ce3597851110001cf6248868fd2996ba346cb94ed4e3d8510544f')

def distance(start, end):
    route = client.directions(
        coordinates=[start, end],
        profile='driving-car',
        format='geojson')
    dist = route['features'][0]['properties']['segments'][0]['distance']
    return dist

def extractMin(distArray):
    coords = []
    q = []

    for index in range(len(clusters)):
        heapq.heappush(q, (distArray[index], clusters[index]))
    for x in range(clustersPerDivision):
        _, coord = heapq.heappop(q)
        coords.append(coord)
    return coords

def createMap(start, stops, division_index):

    m = folium.Map(location=[1.290270, 103.851959], zoom_start=10, control_scale=True, tiles="cartodbpositron")

    folium.Marker(
        location=list(start[::-1]),
        popup="AMK police division",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    for index in range(len(stops)):
        folium.Marker(
            location=list(stops[index][::-1]),
            popup=f"Cluster {index}",
            icon=folium.Icon(color="red"),
        ).add_to(m)

    vehicle_start = start
    vehicles = [
        ors.optimization.Vehicle(id=0, profile='driving-car', start=vehicle_start, end=vehicle_start, capacity=[5])
    ]
    jobs = [ors.optimization.Job(id=i, location=stop, amount=[1]) for i, stop in enumerate(stops)]
    optimized = client.optimization(jobs=jobs, vehicles=vehicles, geometry=True)
    line_color = 'blue'
    for route in optimized['routes']:
        folium.PolyLine(locations=[list(reversed(coord)) for coord in ors.convert.decode_polyline(route['geometry'])['coordinates']], color=line_color).add_to(m)

    output_path = f'./myproject/myapp/templates/map{division_index}.html'
    m.save(output_path)

for marker_index, start in enumerate(divisions):
    distArray = []
    for cluster in clusters:
        dist = distance(start, cluster)
        distArray.append(dist)
    
    coords = extractMin(distArray)
    createMap(start, coords, marker_index)