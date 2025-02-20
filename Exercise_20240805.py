# Use Python to access the United States Geological Survey free API and 
# download real-time earthquake events. The API endpoint to get earthquake data is as follows:
# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson
# Program should be able to save the downloaded data in a CSV file.
# Headers - Magnitude, Location, Latitude, Longitude

from datetime import datetime
import requests

r = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson")

data = r.json()['features']

csvData = []

for i in data:
    csvData.append({'mag': i['properties']['mag'], 
    'location': i['properties']['place'], 
    'latitude': i['geometry']['coordinates'][1], 
    'longitude': i['geometry']['coordinates'][0]})

filename = 'EarthquakeData_'+datetime.now().strftime("%Y%m%d%H%M%S")+'.csv'

with open(filename, 'w', encoding='utf-8') as file:
    file.write("Magnitude,Location,Latitude,Longitude\n")
    for i in csvData:
        file.write(f"{i['mag']},\"{i['location']}\",{i['latitude']},{i['longitude']}\n")
