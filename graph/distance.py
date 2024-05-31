import openrouteservice as ors

client = ors.Client(key='5b3ce3597851110001cf6248868fd2996ba346cb94ed4e3d8510544f')

point1 = [103.84508966643547, 1.3850969869082566] # AMK
point2 = [103.79446206, 1.42544815]               # 1st cluster

route = client.directions(
    coordinates=[point1, point2],
    profile='driving-car',
    format='geojson'
)

distance = route['features'][0]['properties']['segments'][0]['distance']

print(f'Distance from point1 to point2: {distance / 1000} km')