import folium 
import pandas as pd
import json

volcanoes = pd.read_csv("volcanoes.txt")
data_json = open ("world.json", 'r', encoding='utf-8-sig').read()
latitude = list(volcanoes['LAT'])
longtitude = list(volcanoes['LON'])
elevation = list(volcanoes["ELEV"])



def elevationColor(elevation):
   
    if elevation < 1000:
        return 'green'

    elif 1000 <= elevation < 3000 :
        return 'orange'
    

map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain")
 
fgv = folium.FeatureGroup( name = "Volcanoes")




for lat, ln, elevation in zip(latitude, longtitude, elevation):
    fgv.add_child(folium.CircleMarker(location=[lat, ln],
                                     popup =str(elevation) + "mt", 
                                     icon = folium.Icon( color = elevationColor(elevation)),
                                     fill = True,
                                     fill_color= elevationColor(elevation), 
                                     color ='grey',
                                     opacity = 0.9))

fgp = folium.FeatureGroup( name = "Population")

fgp.add_child(folium.GeoJson(data=data_json,
                             style_function = lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000 
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                            else  'red' }))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")


