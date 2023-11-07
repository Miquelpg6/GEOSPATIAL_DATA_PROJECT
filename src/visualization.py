import requests
import json
import pandas as pd
from getpass import getpass
import folium
import os
from dotenv import load_dotenv
load_dotenv() # load_env
token = os.getenv("token")
from pymongo import MongoClient
import time
client = MongoClient("localhost:27017")

import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd

client

def read_csv_to_dataframe(file_path):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)
    return df


def build_map(df, type, map):
    for _, row in df.iterrows():
        if type == 'starbucks':
            icon = folium.Icon(
                color = "beige",
                icon_color = "white",
                icon = "fa-coffee",
                prefix = "fa",
            )
        if type == 'design':
            icon = folium.Icon(
                color = "darkblue",
                icon_color = "white",
                icon = "palette",
                prefix = "fa",
            )
        if type == 'bars':
            icon = folium.Icon(
                color = "black",
                icon_color = "white",
                icon = "beer-mug-empty",
                prefix = "fa",
            )
        if type == 'airport':
            icon = folium.Icon(
                color = "orange",
                icon_color = "white",
                icon = "fa-paper-plane",
                prefix = "fa",
            )
        if type == 'school':
            icon = folium.Icon(
                color = "lightred",
                icon_color = "white",
                icon = "fa-graduation-cap",
                prefix = "fa",
            )
        if type == 'vegan':
            icon = folium.Icon(
                color = "green",
                icon_color = "white",
                icon = "seedling",
                prefix = "fa",
            )
        
        new_marker = folium.Marker(location = [row["lat"], row["lon"]], icon=icon)
        new_marker.add_to(map)





def visualization():

    lat_mo =  45.508210
    lon_mo = -73.568340 

    tor_lat = 43.654770 
    tor_lon = -79.392346

    ott_lat = 45.409977
    ott_lon = -75.701231


    df_bars_mo = read_csv_to_dataframe("DATA/bars_mo.csv")
    df_schools_mo = read_csv_to_dataframe("DATA/schools_mo.csv")
    df_air_mo = read_csv_to_dataframe("DATA/air_mo.csv")
    df_starbucks_mo = read_csv_to_dataframe("DATA/starbucks_mo.csv")
    df_design_mo = read_csv_to_dataframe("DATA/design_mo.csv")
    df_vegan_mo = read_csv_to_dataframe("DATA/vegan_mo.csv")


    df_bars_to = pd.read_csv("DATA/bars_to.csv")
    df_schools_to = pd.read_csv("DATA/schools_to.csv")
    df_air_to = pd.read_csv("DATA/air_to.csv")
    df_starbucks_to = pd.read_csv("DATA/starbucks_to.csv")
    df_design_to = pd.read_csv("DATA/design_to.csv")
    df_vegan_to = pd.read_csv("DATA/vegan_to.csv")


    df_bars_ot = pd.read_csv("DATA/bars_ot.csv")
    df_schools_ot = pd.read_csv("DATA/schools_ot.csv")
    df_air_ot = pd.read_csv("DATA/air_ot.csv")
    df_starbucks_ot = pd.read_csv("DATA/starbucks_ot.csv")
    df_design_ot = pd.read_csv("DATA/design_ot.csv")
    df_vegan_ot = pd.read_csv("DATA/vegan_ot.csv")


# MAP MONTREAL

    map_mo = Map(location = [lat_mo, lon_mo], zoom_start=12)

    build_map(df_bars_mo, 'bars', map_mo)
    build_map(df_schools_mo, 'school', map_mo)
    build_map(df_air_mo, 'airport', map_mo)
    build_map(df_starbucks_mo, 'starbucks', map_mo)
    build_map(df_design_mo, 'design', map_mo)
    build_map(df_vegan_mo, 'vegan', map_mo)

    map_mo.save('GRAPHS/FINAL_MONTREAL.html')


# MAP TORONTO

    map_to = Map(location = [tor_lat, tor_lon], zoom_start=11)

    build_map(df_bars_to, 'bars', map_to)
    build_map(df_schools_to, 'school', map_to)
    build_map(df_air_to, 'airport', map_to)
    build_map(df_starbucks_to, 'starbucks', map_to)
    build_map(df_design_to, 'design', map_to)
    build_map(df_vegan_to, 'vegan', map_to)

    map_to.save('GRAPHS/FINAL_TORONTO.html')


# MAP OTTAWA

    map_ot = Map(location = [ott_lat, ott_lon], zoom_start=11)

    build_map(df_bars_ot, 'bars', map_ot)
    build_map(df_schools_ot, 'school', map_ot)
    build_map(df_air_ot, 'airport', map_ot)
    build_map(df_starbucks_ot, 'starbucks', map_ot)
    build_map(df_design_ot, 'design', map_ot)
    build_map(df_vegan_ot, 'vegan', map_ot)

    map_ot.save("GRAPHS/FINAL_OTTAWA.html")