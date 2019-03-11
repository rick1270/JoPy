#!/usr/bin/python

# import libraries... insert into libraries where appropriate

import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt
from urllib.request import urlopen
from PIL import Image
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import math
import colorsys
# list of dependencies

# enter google maps api key


def api(api):
    api = api
    print("Google Maps API (" + str(api) + ") has been logged in JoPy")

# create square static map image


def square_map(map_center, zoom_level, map_type):
    from geopy.geocoders import Nominatim
    from urllib.request import urlopen
    import math

    if (zoom_level <= 0 or zoom_level > 23):
        raise ValueError("zoom_level is outside Google Maps parameters (1-24)")
    # locked map size... change to optional image size later
    width = 600
    height = 600
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    center_clean = geolocator.geocode(map_center.replace('+', ' '))
    center_lat = float(center_clean.latitude)
    center_long = float(center_clean.longitude)
    km_px = (156543.03392 * math.cos(center_lat * math.pi/180)/math.pow(2,
             (zoom_level)))/1000
    center_0_http = str(center_lat) + ',' + str(center_long)
    endpoint = 'https://maps.googleapis.com/maps/api/staticmap?'
    map_url = str(endpoint) + 'center=' + str(center_0_http) 
    + '&zoom=' + (zoom_level) + '&size=' + str(width) + 'x' + str(height) 
    + '&maptype=' + str(map_type) + '&key=' + str(api)
    map_img = Image.open(urlopen(map_url))
    map_img
