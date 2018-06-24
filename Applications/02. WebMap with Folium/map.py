import folium
import pandas

map = folium.Map(location = [38.58,-99.09], zoom_start = 6)
data = pandas.read_csv("Volcanoes_USA.txt")
#print(data)
list_lat = list(data['LAT'])
list_lon = list(data['LON'])
list_nam = list(data['NAME'])
list_elv = list(data['ELEV'])

def color_produce(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

#Feature Group Vulcano
fgv = folium.FeatureGroup(name = "Vulcano")

for i,j, elev in zip(list_lat, list_lon,list_elv):
    fgv.add_child(folium.CircleMarker(location = [i,j], radius = 6, popup = str(elev), fill = True, fill_color = color_produce(elev), color = color_produce(elev)))

#Feature Group Color
fgp = folium.FeatureGroup(name = "Color")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = 'utf-8-sig').read()))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
