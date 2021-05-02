import folium
import pandas

data=pandas.read_csv('Volcanoes.txt')
# Get list of columns in the dataframe
# data.columns
lat=list(data['LAT'])
lon=list(data['LON'])

map=folium.Map(location=(lat[0], lon[0]), zoom_start=6, tiles="Stamen Terrain")

fg=folium.FeatureGroup(name="Map of an interesting location")

# Iterate over multiple lists with `zip`
for lt,ln in zip(lat,lon):
    coords=(lt, ln)
    fg.add_child(folium.Marker(coords, popup="A location somewhere close to Montreal", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save('map.html')
