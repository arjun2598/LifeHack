import random
import csv

# Singapore's mainland boundaries (approximated for simplicity):
# Latitude: 1.2 to 1.5
# Longitude: 103.6 to 104.0

# Function to generate random coordinates
def generate_random_coordinates(n, lat_range, lon_range):
    coordinates = []
    for _ in range(n):
        lat = random.uniform(lat_range[0], lat_range[1])
        lon = random.uniform(lon_range[0], lon_range[1])
        coordinates.append((lat, lon))
    return coordinates

# Generate 500 random coordinates
num_coordinates = 250
lat_range = (1.296918, 1.412878)
lon_range = (103.739994, 103.900289)

coordinates = generate_random_coordinates(num_coordinates, lat_range, lon_range)

# Define the CSV file path
file_path = '/Users/arjun/Documents/GitHub/LifeHack/clustering/random_coordinates_singapore.csv'

# Write the coordinates to a CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Latitude", "Longitude"])
    writer.writerows(coordinates)

file_path
