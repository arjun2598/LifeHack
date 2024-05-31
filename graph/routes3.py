import openrouteservice as ors
import folium
import heapq

# Coordinate list
markers = [
    [103.84508966643547, 1.3850969869082566],  # AMK
    [103.93716055293469, 1.3328855285307624],  # Bedok
    [103.83975222595029, 1.278604029532352],   # Central
    [103.70234408177062, 1.3511457864334573],  # Jurong
    [103.84670982409857, 1.3123442012770405],  # Tanglin
    [103.77883793759092, 1.4332850043061145],  # Woodlands
    [103.98103923150593, 1.3431877727562795]   # Airport
]
# Cluster list
clusters = [
    [103.9649901, 1.45851241],
    [103.65907719, 1.32529109],
    [103.83958907, 1.3187313],
    [103.79446206, 1.42544815],
    [103.63232582, 1.45563023],
    [103.94987974, 1.37352285],
    [103.75372947, 1.36926662],
    [103.94423368, 1.31254137]
]

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

for marker_index, start in enumerate(markers):
    distArray = []
    for cluster in clusters:
        dist = distance(start, cluster)
        distArray.append(dist)
    
    coords = extractMin3(distArray)
    createMap(start, coords, marker_index)