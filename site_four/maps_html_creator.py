"""to execute on your PC"""
"""pip install folium"""
"""pip install pandas"""

import folium
import pandas as pd
import os
import json

countries = os.path.join('data', 'countries_world.json')
covid_data = os.path.join('data', 'Data_covid_numbers.csv')
state_data = pd.read_csv(covid_data)

#Create map with starting location, design and zoom
m = folium.Map(location=[47,12], tiles='cartodbpositron', zoom_start=5)

#Overlay
m.choropleth(
    geo_data=countries,
    name='layer',
    data=state_data,
    columns=['iso_code','current_cases'],
    key_on='feature.id',
    fill_color='YlOrRd',
    fill_opacity=0.6,
    line_opacity=0.0,
    legend_name='Current COVID-19 cases')

#Global tooltip
tooltip ='Click for more Info'

#Vega data
vis_austria  = os.path.join('data', 'visualization.austria.vg.json')
vis  = os.path.join('data', 'vis.json')

#Create markers
"""folium.Marker([47.149659, 9.516347],
              popup='<strong><a href="https://www.uni.li/">Visit Uni.li!</a></strong>',
              icon=folium.Icon(color='red'),
              tooltip=tooltip).add_to(m)"""

folium.Marker([47.510081, 14.059615],
              popup='<strong><a href="https://www.sozialministerium.at/Informationen-zum-Coronavirus/Coronavirus---Aktuelle-Ma%C3%9Fnahmen.html">Corona Info Austria</a></strong>',
              icon=folium.Icon(color='red'),
              tooltip=tooltip).add_to(m)

#marker Switzerland
folium.Marker([47.126709, 8.339258],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis))))).add_to(m)

#marker Austria
folium.Marker([47.261086, 11.788965],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis_austria))))).add_to(m)

#marker Liechtenstein
folium.Marker([47.117756, 9.562807],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis))))).add_to(m)

#marker Germany
folium.Marker([50.495392, 10.121229],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis))))).add_to(m)



#Circle
folium.CircleMarker(
    location=[47.149659, 9.516347],
    radius=15,
    popup='',
    color='#FF0000',
    fill=True,
    fill_color='#8B0000'
).add_to(m)


folium.LayerControl().add_to(m)
#Create map to cd site_four
m.save('templates/site_four/base.html')
