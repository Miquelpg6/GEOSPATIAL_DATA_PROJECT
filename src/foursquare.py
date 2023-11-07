import os
import requests
import json
from dotenv import load_dotenv
import pandas as pd

import geopandas as gpd
from cartoframes.viz import Map, Layer, popup_element

import os
from dotenv import load_dotenv
load_dotenv() 

token = os.getenv("token")


def requests_for_foursquare (query, lat, lon, radius, limit=40):

    url = f"https://api.foursquare.com/v3/places/search?query={query}&ll={lat}%2C{lon}&radius={radius}&limit={limit}"

    headers = {
        "accept": "application/json",
        "Authorization": token
    }
    
    try:
        return requests.get(url, headers=headers).json()
    except:
        print("no :(")


def extracting_from_one_element (general):

    name = general["name"]
    address = general["location"]["address"]
    distance = general["distance"]
    zip_code = general["location"]["postcode"]
    lat = general["geocodes"]["main"]["latitude"]
    lon = general["geocodes"]["main"]["longitude"]

    
    small_dict = {
    "name": name,
    "address": address,
    "zip_code": zip_code,
    "distance": distance,
    "lat": lat,
    "lon": lon
    }
    return small_dict

def transform_request_into_df (res):
    list_of_dictionaries = [extracting_from_one_element (element) for element in res["results"]]
    return pd.DataFrame(list_of_dictionaries)


def foursquare():

    lat_mo =  45.508210
    lon_mo = -73.568340

    tor_lat = 43.654770 
    tor_lon = -79.392346

    ott_lat = 45.409977
    ott_lon = -75.701231

#BARS
#bars montreeal

    bars_mo = requests_for_foursquare ("beer", lat_mo, lon_mo, radius=1000, limit = 28)
    df_bars_mo = transform_request_into_df (bars_mo)

    df_bars_mo.to_csv("DATA/bars_mo.csv")

# toronto

    bars_to = requests_for_foursquare ("beer", tor_lat, tor_lon, radius=1000, limit=27)
    df_bars_to = transform_request_into_df (bars_to)

    df_bars_to.to_csv("DATA/bars_to.csv")

#ottawa

    bars_ot = requests_for_foursquare ("beer", ott_lat, ott_lon, radius=1000, limit=50)
    df_bars_ot = transform_request_into_df (bars_ot)

    df_bars_ot.to_csv("DATA/bars_ot.csv")


#SCHOOLS

    schools_mo = requests_for_foursquare ("schools", lat_mo, lon_mo, radius=2000, limit=18)
    df_sch_mo = transform_request_into_df (schools_mo)

    df_sch_mo.to_csv("DATA/schools_mo.csv")


#TORONTO

    schools_to = requests_for_foursquare ("schools", tor_lat, tor_lon, radius=2000, limit=20)
    df_sch_to = transform_request_into_df (schools_to)

    df_sch_to.to_csv("DATA/schools_to.csv")

#OTTAWA

    schools_ot = requests_for_foursquare ("schools", ott_lat, ott_lon, radius=2000, limit=10)
    df_sch_ot = transform_request_into_df (schools_ot)

    df_sch_ot.to_csv("DATA/schools_ot.csv")

#AIRPORTS

#MONTREAL
    plane_mo = requests_for_foursquare (("airport"), lat_mo, lon_mo, radius= 25000, limit=1)
    df_plane_mo = transform_request_into_df (plane_mo)

    df_plane_mo.to_csv("DATA/air_mo.csv")

#TORONTO

    plane_to = requests_for_foursquare ("Aéroport", tor_lat, tor_lon, radius=20000, limit=2)
    df_plane_to = transform_request_into_df (plane_to)

    df_plane_to.to_csv("DATA/air_to.csv")

#OTTAWA

    plane_ot = requests_for_foursquare ("Airport", ott_lat, ott_lon, radius=20000, limit=1)
    df_plane_ot= transform_request_into_df (plane_ot)

    df_plane_ot.to_csv("DATA/air_ot.csv")


#STARBUCKS

#MONTREAL

    starbucks_mo = requests_for_foursquare ("Starbucks", lat_mo, lon_mo, radius=1000, limit=10)
    df_starbucks_mo= transform_request_into_df (starbucks_mo)

    df_starbucks_mo.to_csv("DATA/starbucks_mo.csv")

# TORONTO

    starbucks_to = requests_for_foursquare ("Starbucks", tor_lat, tor_lon, radius=1000, limit=10)
    df_starbucks_to = transform_request_into_df (starbucks_to)

    df_starbucks_to.to_csv("DATA/starbucks_to.csv")

#OTTAWA

    starbucks_ot = requests_for_foursquare ("Starbucks", ott_lat, ott_lon, radius=1000, limit=10)
    df_starbucks_ot = transform_request_into_df (starbucks_ot)

    df_starbucks_ot.to_csv("DATA/starbucks_ot.csv")


#DESIGN

#MONTREAL

    design_mo = requests_for_foursquare ("design", lat_mo, lon_mo, radius=1000, limit=4)
    df_design_mo = transform_request_into_df (design_mo)

    df_design_mo.to_csv("DATA/design_mo.csv")

#TORONTO
    design_to = requests_for_foursquare ("design", tor_lat, tor_lon, radius=1000, limit=19)
    df_design_to = transform_request_into_df (design_to)    

    df_design_to.to_csv("DATA/design_to.csv")

#OTTAWA

    design_ot = requests_for_foursquare ("Design", ott_lat, ott_lon, radius=1000, limit=5)
    df_design_ot = transform_request_into_df (design_ot)

    df_design_ot.to_csv("DATA/design_ot.csv")

#VEGAN

#MONTREAL

    vegan_mo = requests_for_foursquare ("vegan", lat_mo, lon_mo, radius=1000, limit=8)
    df_vegan_mo = transform_request_into_df (vegan_mo)

    df_vegan_mo.to_csv("DATA/vegan_mo.csv")

#TORONTO

    vegan_to = requests_for_foursquare ("vegan restaurant", tor_lat, tor_lon, radius=1000, limit=40)
    df_vegan_to = transform_request_into_df (vegan_to)

    df_vegan_to.to_csv("DATA/vegan_to.csv")

#OTTAWA

    vegan_ot = requests_for_foursquare ("vegan restaurant", ott_lat, ott_lon, radius=1000, limit=20)
    df_vegan_ot = transform_request_into_df (vegan_ot)

    df_vegan_ot.to_csv("DATA/vegan_ot.csv")


