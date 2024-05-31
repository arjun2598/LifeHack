import openrouteservice as ors
import folium

client = ors.Client(key='5b3ce3597851110001cf6248868fd2996ba346cb94ed4e3d8510544f')

start = [103.84508966643547, 1.3850969869082566] #AMK
test1 = [103.79446206,  1.42544815]
test2 = [103.65907719, 1.32529109]
test3 = [103.83958907, 1.3187313]

coords = [test1, test2, test3]

m = folium.Map(location=[1.290270, 103.851959],zoom_start=10, control_scale=True,tiles="cartodbpositron")

folium.Marker(
    location=list(start[::-1]),
    popup="AMK police division",
    icon=folium.Icon(color="green"),
).add_to(m)

folium.Marker(
    location=list(coords[0][::-1]),
    popup="1st cluster",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=list(coords[1][::-1]),
    popup="2nd cluster",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=list(coords[2][::-1]),
    popup="3rd cluster",
    icon=folium.Icon(color="red"),
).add_to(m)

vehicle_start = start
vehicles = [
    ors.optimization.Vehicle(id=0, profile='driving-car', start=vehicle_start, end=vehicle_start, capacity=[5])
]
jobs = [ors.optimization.Job(id=index, location=coords, amount=[1]) for index, coords in enumerate(coords)]
optimized = client.optimization(jobs=jobs, vehicles=vehicles, geometry=True)
line_color = 'blue'
for route in optimized['routes']:
    folium.PolyLine(locations=[list(reversed(coords)) for coords in ors.convert.decode_polyline(route['geometry'])['coordinates']], color=line_color).add_to(m)


m.save('map.html')