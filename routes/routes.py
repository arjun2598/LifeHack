import openrouteservice as ors
import folium
import heapq
import pandas as pd

# Create Division list
def read_file(file):
    df = pd.read_csv(file)
    df1 = df[["Longitude", "Latitude"]]
    return df1.values.tolist()

divisions = read_file("./divisions.csv")

# Cluster list
clusters = [[103.8894943,    1.37137097],
 [103.75384243,   1.32832649],
 [103.85647599,   1.31489651],
 [103.85213785,   1.37308564],
 [103.74797244,   1.37611672],
 [103.80851027,   1.31020939],
 [103.88943683,   1.34034548],
 [103.85146252,   1.39520717],
 [103.781162,     1.32403574],
 [103.761995,     1.30888776],
 [103.83797321,   1.34133769],
 [103.87743181,   1.40296949],
 [103.89002772,   1.31193853],
 [103.82559335,   1.39025353],
 [103.87247191,   1.36156713]]

client = ors.Client(key='5b3ce3597851110001cf6248868fd2996ba346cb94ed4e3d8510544f')

def distance(start, end):
    route = client.directions(
        coordinates=[start, end],
        profile='driving-car',
        format='geojson')
    dist = route['features'][0]['properties']['segments'][0]['distance']
    return dist

def extractMin3(distArray):
    coords = []
    q = []

    for index in range(len(clusters)):
        heapq.heappush(q, (distArray[index], clusters[index]))
    for x in range(3):
        _, coord = heapq.heappop(q)
        coords.append(coord)
    return coords

def createMap(start, stops, index):

    m = folium.Map(location=[1.290270, 103.851959], zoom_start=10, control_scale=True, tiles="cartodbpositron")

    folium.Marker(
        location=list(start[::-1]),
        popup="AMK police division",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    folium.Marker(
        location=list(stops[0][::-1]),
        popup="1st cluster",
        icon=folium.Icon(color="red"),
    ).add_to(m)

    folium.Marker(
        location=list(stops[1][::-1]),
        popup="2nd cluster",
        icon=folium.Icon(color="red"),
    ).add_to(m)

    folium.Marker(
        location=list(stops[2][::-1]),
        popup="3rd cluster",
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

    m.save(f'map{index}.html')

for marker_index, start in enumerate(divisions):
    distArray = []
    for cluster in clusters:
        dist = distance(start, cluster)
        distArray.append(dist)
    
    coords = extractMin3(distArray)
    createMap(start, coords, marker_index)