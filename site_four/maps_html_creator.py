"""to execute on your PC """
"""pip install folium"""
"""pip install pandas"""

import folium
import pandas as pd
import os

countries = os.path.join('data', 'countries_world.json')
covid_data = os.path.join('data', 'Data_covid_numbers.csv')
state_data = pd.read_csv(covid_data)

#Create map with start location, design and zoom
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

#Create markers
folium.Marker([47.149659, 9.516347],
              popup='<strong><a href="https://www.uni.li/">Visit Uni.li!</a></strong>',
              tooltip=tooltip).add_to(m)



folium.LayerControl().add_to(m)
#Create map to cd site_four
m.save('templates/site_four/base.html')
