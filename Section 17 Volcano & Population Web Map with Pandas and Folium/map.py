import folium
import pandas

data=pandas.read_csv('Volcanoes.txt')
# Get list of columns in the dataframe
# data.columns
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])

def color_maker(elevation):
    if elevation<1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=(lat[0], lon[0]), zoom_start=6, tiles="Stamen Terrain")
fg=folium.FeatureGroup(name="Map of an interesting location")
html="""<h4>Volcano information:</h4>
Height: %s m
"""

# Iterate over multiple lists with `zip`
# for lt,ln,el in zip(lat,lon,elev):
#     coords=(lt, ln)
#     iframe=folium.IFrame(html=html % str(el), width=200, height=100)
#     fg.add_child(folium.Marker(coords, popup=folium.Popup(iframe), icon=folium.Icon(color=color_maker(el))))
#     # fg.add_child(folium.Marker(coords, popup=folium.Popup(str(el)+' m', parse_html=True), icon=folium.Icon(color='green')))

for lt,ln,el in zip(lat,lon,elev):
    coords=(lt, ln)
    iframe=folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.CircleMarker(coords, radius=6, popup=folium.Popup(iframe), 
    fill_color=color_maker(el), fill=True, fill_opacity=1.0, color='grey'))
    # fg.add_child(folium.Marker(coords, popup=folium.Popup(str(el)+' m', parse_html=True), icon=folium.Icon(color='green')))

map.add_child(fg)
map.save('map.html')
