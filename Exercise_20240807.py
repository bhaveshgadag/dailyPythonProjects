# Utilize the CSV file produced by that program. Create a map of earthquakes using that CSV file.
# Each earthquake is represented by a circle and the circle radius represents the magnitude of the earthquakes.
# When the user hovers the cursor over a circle, a popup shows the location description of the earthquake.
# Use the Python folium library to produce the map and optionally, 
# streamlit and streamlit-folium to embed the map in a streamlit website. 

import folium

with open("EarthquakeData_20250219212746.csv", 'r',encoding='utf-8') as file:
    earthquakeData = file.readlines()
    eData = []
    for i in range(1,len(earthquakeData)):
        temp = earthquakeData[i].split(sep='"')
        temp[0] = float(temp[0].rstrip(','))
        temp[2] = temp[2].strip(',').rstrip()
        temp.extend(temp[2].split(','))
        temp.pop(2)
        eData.append(temp)

m = folium.Map(location=(42.52, -124.67))

for element in eData:
    folium.Circle(
        location=[element[2], element[3]],
        radius=element[0]*1000,
        color="black",
        weight=1,
        fill_opacity=0.6,
        opacity=1,
        fill_color="green",
        fill=False,  # gets overridden by fill_color
        tooltip=element[1],
    ).add_to(m)

m.save("index.html")