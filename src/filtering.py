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
db = client["ironhack"]
c = db.get_collection("companies")


def get_companies_dataframe(collection, conditions, projection):
    # Use the find method to retrieve the matching documents
    companies = list(collection.find(conditions, projection))


    # Create a Pandas DataFrame from the list of documents
    df = pd.json_normalize(companies, "offices", ["name"])
    df = df.rename(columns={"latitude": "company_latitude", "longitude": "company_longitude"})

    # Drop rows with NaN values
    df = df.dropna()

    return df

def save_dataframe_to_csv(dataframe, file_path):
    # Save the DataFrame to the specified CSV file
    dataframe.to_csv(file_path, index=False)

def create_map_with_markers(dataframe, lat_column, lon_column, map_location, zoom_level):
    # Create a folium map
    map_ = folium.Map(location=map_location, zoom_start=zoom_level)
    
    for index, row in dataframe.iterrows():
        lat_accident = row[lat_column]
        lon_accident = row[lon_column]
        new_marker = folium.Marker(location=[lat_accident, lon_accident])
        new_marker.add_to(map_)
    
    return map_

def create_heatmap(dataframe, lat_column, lon_column, zoom_level, location):
    # Create a folium map
    map_ = folium.Map(location=location, zoom_start=zoom_level)
    
    # Create a heat map layer
    heat_map = HeatMap(data=dataframe[[lat_column, lon_column]])
    
    # Add the heat map to the map
    heat_map.add_to(map_)
    
    return map_






def filtering_companies ():

    zoom_level = 12

#MONTREAL

    conditions_mo = {"$and": [{"offices.city": "Montreal"}, {}]}
    projection_mo = {"name": 1, "_id": 0, "offices.latitude": 1, "offices.longitude": 1}

    lat_mo = 45.502033 
    lon_mo = -73.622622 
    location_mo = [lat_mo, lon_mo]



# TORONTO

    conditions_to = {"$and": [{"offices.city": "Toronto"}, {}]}
    projection_to = {"name": 1, "_id": 0, "offices.latitude": 1, "offices.longitude": 1}   

    tor_lat = 43.719256 
    tor_lon = -79.379482
    location_tor = [tor_lat, tor_lon]


    

#OTTAWA

    conditions = {"$and": [{"offices.city": "Ottawa"}, {}]}
    projection = {"name": 1, "_id": 0, "offices.latitude": 1, "offices.longitude": 1}

    ott_lat = 45.409977
    ott_lon = -75.701231
    location_ot = [ott_lat, ott_lon]




#MONTREAL
    df_mo = get_companies_dataframe(c, conditions_mo, projection_mo)
    df_mo

    map_mo = create_map_with_markers(df_mo, "company_latitude", "company_longitude", [lat_mo, lon_mo], zoom_level)
    map_mo.save("GRAPHS/montreal_map.html")

    
    zoom_level = 12
    map_ht_mo = create_heatmap(df_mo, "company_latitude", "company_longitude", zoom_level, location_mo)
    map_ht_mo.save('GRAPHS/montreal_heat_map.html')

#TORONTO

    df_to = get_companies_dataframe(c, conditions_to, projection_to)
    df_to

    map_to = create_map_with_markers(df_to, "company_latitude", "company_longitude", [tor_lat, tor_lon], zoom_level)
    map_to.save('GRAPHS/toronto_map.html')
    
    zoom_level = 11
    map_ht_to = create_heatmap(df_to, "company_latitude", "company_longitude", zoom_level, location_tor)
    map_ht_to.save('GRAPHS/toronto_heat_map.html')

# OTTAWA

    df_ot = get_companies_dataframe(c, conditions, projection)
    df_ot

    map_ot = create_map_with_markers(df_ot, "company_latitude", "company_longitude", [ott_lat, ott_lon], zoom_level)
    map_ot.save('GRAPHS/ottawa_map.html')

    zoom_level = 11
    map_ht_ot = create_heatmap(df_ot, "company_latitude", "company_longitude", zoom_level, location_ot)
    map_ht_ot.save('GRAPHS/ottawa_heat_map.html')