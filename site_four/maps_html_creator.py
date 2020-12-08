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
aus = os.path.join('data', 'austria.json')
ger = os.path.join('data', 'germany.json')
fli = os.path.join('data', 'liechtenstein.json')
sch = os.path.join('data', 'switzerland.json')

#Create markers
#Info Marker Austria
folium.Marker([48.214945, 16.417481],
              popup='<strong><a href="https://www.sozialministerium.at/Informationen-zum-Coronavirus/Coronavirus---Aktuelle-Ma%C3%9Fnahmen.html">Corona Info Austria</a></strong>',
              icon=folium.Icon(color='red'),
              tooltip=tooltip).add_to(m)

#Info Marker Germany
folium.Marker([52.411964, 13.406485],
              popup='<strong><a href="https://www.bundesgesundheitsministerium.de/coronavirus.html">Corona Info Germany</a></strong>',
              icon=folium.Icon(color='red'),
              tooltip=tooltip).add_to(m)

#Info Marker Liechtenstein
folium.Marker([47.146309, 9.528885],
              popup='<strong><a href="https://www.regierung.li/coronavirus">Corona Info Liechtenstein</a></strong>',
              icon=folium.Icon(color='red'),
              tooltip=tooltip).add_to(m)

#Info Marker Switzerland
folium.Marker([46.936296, 7.506603],
              popup='<strong><a href="https://www.bag.admin.ch/bag/de/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/situation-schweiz-und-international.html">Corona Info Switzerland</a></strong>',
              icon=folium.Icon(color='red'),
              tooltip=tooltip).add_to(m)



#Austria_New_Cases
folium.Marker([47.818428, 14.373676],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(aus))))).add_to(m)

#Germany_New_Cases
folium.Marker([51.430192, 10.153662],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(ger))))).add_to(m)

#Liechtenstein_New_Cases
folium.Marker([47.087587, 9.551893],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(fli))))).add_to(m)

#Switzerland_New_Cases
folium.Marker([46.460855, 8.077289],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(sch))))).add_to(m)



#Circle
folium.CircleMarker(
    location=[47.149659, 9.516347],
    radius=4,
    popup='',
    color='#FF0000',
    fill=True,
    fill_color='#8B0000'
).add_to(m)


folium.LayerControl().add_to(m)
#Create map to cd site_four
m.save('templates/site_four/base.html')
