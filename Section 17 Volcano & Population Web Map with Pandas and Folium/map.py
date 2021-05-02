import folium
import pandas

data=pandas.read_csv('Volcanoes.txt')
# Get list of columns in the dataframe
# data.columns
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])

map=folium.Map(location=(lat[0], lon[0]), zoom_start=6, tiles="Stamen Terrain")

fg=folium.FeatureGroup(name="Map of an interesting location")

# Iterate over multiple lists with `zip`
for lt,ln,el in zip(lat,lon,elev):
    coords=(lt, ln)
    fg.add_child(folium.Marker(coords, popup=folium.Popup(str(el)+'m', parse_html=True), icon=folium.Icon(color='green')))

map.add_child(fg)
map.save('map.html')
