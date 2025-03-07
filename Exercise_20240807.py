# Utilize the CSV file produced by that program. Create a map of earthquakes using that CSV file.
# Each earthquake is represented by a circle and the circle radius represents the magnitude of the earthquakes.
# When the user hovers the cursor over a circle, a popup shows the location description of the earthquake.
# Use the Python folium library to produce the map and optionally, 
# streamlit and streamlit-folium to embed the map in a streamlit website. 

import folium

with open("EarthquakeData_20250219212746.csv", 'r',encoding='utf-8') as file:
    earthquakeData = file.readlines()
    eData = []
    for i in range(1,3):
        temp = earthquakeData[i].split(sep='"')
        temp[0] = temp[0].rstrip(',')
        temp[2] = temp[2].strip(',').rstrip()
        temp.extend(temp[2].split(','))
        temp.pop(2)
        eData.append(temp)
        

for i in range(len(eData)):
    print(eData[i])    
# m = folium.Map(location=(45.52, -112.67))

# folium.CircleMarker((earthquakeData[1][2],earthquakeData[1][3]),earthquakeData[1][0],tooltip=earthquakeData[1][1]) 

# m.save("index.html")