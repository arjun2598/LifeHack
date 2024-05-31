import openrouteservice as ors
import folium
import heapq

# Coordinate list
markers = [
            [103.84508966643547, 1.3850969869082566], # AMK
            [103.93716055293469, 1.3328855285307624], # Bedok
            [103.83975222595029, 1.278604029532352],  #Central' },
            [103.70234408177062, 1.3511457864334573], #Jurong' },
            [103.84670982409857, 1.3123442012770405], #Tanglin' },
            [103.77883793759092, 1.4332850043061145], #Woodlands' },
            [103.98103923150593, 1.3431877727562795]  #Airport' },
        ]
# cluster list
clusters = [[103.9649901, 1.45851241],
 [103.65907719, 1.32529109],
 [103.83958907,   1.3187313 ],
 [103.79446206,  1.42544815],
 #[103.97510551,   1.24519526],
 [103.63232582,   1.45563023],
 [103.94987974,   1.37352285],
 # [103.757965,     1.22426563],
 #[103.63411352,  1.23252144],
 #[103.89968689,   1.23929927],
 #[103.69616227,   1.44534602],
 #[103.87769813,   1.39104981],
 #[103.6217795,    1.37393365],
 #[103.8683841,    1.47237248],
 #[103.75131769,   1.28925117],
 #[103.84002844,   1.23518758],
 [103.75372947,   1.36926662],
 [103.94423368,   1.31254137]]
 #[103.79347757,   1.47873739],
 #[103.6930949,    1.24406834]]

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
        coords.append(heapq.heappop(q))
    return coords

def createMap(start, stops, index):

    m = folium.Map(location=[1.290270, 103.851959],zoom_start=10, control_scale=True,tiles="cartodbpositron")

    folium.Marker(
        location=list(start[::-1]),
        popup="AMK police division",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    '''
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
    '''

    vehicle_start = start
    vehicles = [
        ors.optimization.Vehicle(id=0, profile='driving-car', start=vehicle_start, end=vehicle_start, capacity=[5])
    ]
    jobs = [ors.optimization.Job(id=index, location=stops, amount=[1]) for index, stops in enumerate(stops)]
    optimized = client.optimization(jobs=jobs, vehicles=vehicles, geometry=True)
    line_color = 'blue'
    for route in optimized['routes']:
        folium.PolyLine(locations=[list(reversed(stops)) for stops in ors.convert.decode_polyline(route['geometry'])['coordinates']], color=line_color).add_to(m)

    m.save('map%s.html' % index)

for index in range(len(markers)):
    start = markers[index]
    distArray = []
    for index in range(len(clusters)):
        dist = distance(start, clusters[index])
        distArray.append(dist)
    
    coords = extractMin3(distArray)
    m = createMap(start, coords, index)
   

