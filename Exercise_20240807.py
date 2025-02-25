# Utilize the CSV file produced by that program. Create a map of earthquakes using that CSV file.
# Each earthquake is represented by a circle and the circle radius represents the magnitude of the earthquakes.
# When the user hovers the cursor over a circle, a popup shows the location description of the earthquake.
# Use the Python folium library to produce the map and optionally, 
# streamlit and streamlit-folium to embed the map in a streamlit website. 

import folium

with open("EarthquakeData_20250219212746.csv", 'r',encoding='utf-8') as file:
    eathquakeData = file.readlines()
    
m = folium.Map(location=(45.52, -112.67))


 