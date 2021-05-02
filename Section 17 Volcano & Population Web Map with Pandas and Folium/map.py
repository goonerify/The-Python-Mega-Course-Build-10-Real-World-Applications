import folium

map=folium.Map(location=(45.505782121361555, -73.56057788606246), zoom_start=6, tiles="Stamen Terrain")

fg=folium.FeatureGroup(name="Map of an interesting location")

for i in range(0, 5):
    delta=i/1.5
    coords=(45.505782121361555+delta, -73.56057788606246+delta)
    fg.add_child(folium.Marker(coords, popup="A location somewhere close to Montreal", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save('map.html')
