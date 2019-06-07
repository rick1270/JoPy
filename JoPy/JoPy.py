#!/usr/bin/python


import pandas as pd
import matplotlib.pyplot as plt
from urllib.request import urlopen
from PIL import Image
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import math

# return google maps api key


def api_info (api):
    print(str(self.gapi))

# return url for static map

def gmap_url(self):
    if (self.zoom_level <= 0 or self.zoom_level > 23):
        raise ValueError("zoom_level is invalid")
    # locked map size... change to variable

    width = 600
    height = 600
    geolocator = Nominatim(user_agent="JoPy")
    center_clean = geolocator.geocode(self.map_center.replace('+', ' '))
    center_lat = float(center_clean.latitude)
    center_long = float(center_clean.longitude)
    self.km_px = (156543.03392 * math.cos(center_lat * math.pi/180)/math.pow(2,
             (self.zoom_level)))/1000
    center_0_http = str(center_lat) + ',' + str(center_long)
    endpoint = 'https://maps.googleapis.com/maps/api/staticmap?'
    map_url = (str(endpoint) + 'center=' + str(center_0_http) + '&zoom=' +
               str(self.zoom_level) + '&size=' + str(width) + 'x' + str(height) +
               '&maptype=' + str(self.map_type) + '&key=' + str(self.gapi))
    return map_url

  # create square static map image


  def gmap_png(self):
    if (self.zoom_level <= 0 or self.zoom_level > 23):
        raise ValueError("zoom_level is invalid")
    # locked map size... change to variable
    width = 600
    height = 600
    geolocator = Nominatim(user_agent="JoPy")
    center_clean = geolocator.geocode(self.map_center.replace('+', ' '))
    center_lat = float(center_clean.latitude)
    center_long = float(center_clean.longitude)
    center_0_http = str(center_lat) + ',' + str(center_long)
    endpoint = 'https://maps.googleapis.com/maps/api/staticmap?'
    map_url = (str(endpoint) + 'center=' + str(center_0_http) + '&zoom=' +
               str(self.zoom_level) + '&size=' + str(width) + 'x' + str(height) +
               '&maptype=' + str(self.map_type) + '&key=' + str(self.gapi))
    map_img = Image.open(urlopen(map_url))
    return map_img

  # print map specs


  def gmap_info(self):
    # locked map size... change to optional image size later
    width = 600
    height = 600
    geolocator = Nominatim(user_agent="JoPy")
    center_clean = geolocator.geocode(self.map_center.replace('+', ' '))
    center_lat = float(center_clean.latitude)
    center_long = float(center_clean.longitude)
    map_rep_width = self.km_px * width
    map_rep_height = self.km_px * height
    center_0 = center_lat, center_long
    center_0_http = str(center_lat) + ',' + str(center_long)
    center_lat_1 = (center_lat + 1, center_long)
    center_long_1 = (center_lat, center_long + 1)
    lat_km = (geodesic(center_0, center_lat_1).km)
    long_km = (geodesic(center_0, center_long_1).km)
    north = center_lat + (((height/2) * self.km_px) / lat_km)
    south = center_lat - (((height/2) * self.km_px) / lat_km)
    east = center_long + (((height/2) * self.km_px) / long_km)
    west = center_long - (((height/2) * self.km_px) / long_km)
    endpoint = ('https://maps.googleapis.com/maps/api/staticmap?')
    map_url = (str(endpoint) + 'center=' + str(center_0_http) + '&zoom=' +
               str(self.zoom_level) + '&size=' + str(width) + 'x' + str(height) +
               '&key=' + str(self.gapi))
    print('The coordinates at the center of the map are: latitude = ' +
          str(center_lat) + ' and longitude = ' + str(center_long) + ' in ' +
          str(center_clean))
    print('The map represents an area ' + str(map_rep_height) +
          ' km high and ' + str(map_rep_width) + ' km wide')
    print('The borders of the map are: North = ' + str(north) +
          ' latitude  South = ' + str(south) + ' latitude  West = ' +
          str(west) + ' longitude  East = ' + str(east) + ' longitude')
    print('The map image is ' + str(height) + ' pixels high by ' +
          str(width) + ' pixels wide with a zoom level of ' + str(self.zoom_level) +
          ' and may be called using "map_img"')
    print('The map url is: ' + map_url)

  # produce plot background


  def g_to_plot(self, grid=False):
    width = 600
    height = 600
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    center_clean = geolocator.geocode(self.map_center.replace('+', ' '))
    center_lat = float(center_clean.latitude)
    center_long = float(center_clean.longitude)
    km_px = (156543.03392 * math.cos(center_lat * math.pi / 180) / math.pow(2,
             int(self.zoom_level)))/1000
    map_rep_width = km_px * width
    map_rep_height = km_px * height
    center_0 = center_lat, center_long
    center_0_http = str(center_lat) + ',' + str(center_long)
    center_lat_1 = (center_lat + 1, center_long)
    center_long_1 = (center_lat, center_long + 1)
    lat_km = (geodesic(center_0, center_lat_1).km)
    long_km = (geodesic(center_0, center_long_1).km)
    north = center_lat + (((height/2) * km_px) / lat_km)
    south = center_lat - (((height/2) * km_px) / lat_km)
    east = center_long + (((height/2) * km_px) / long_km)
    west = center_long - (((height/2) * km_px) / long_km)
    endpoint = 'https://maps.googleapis.com/maps/api/staticmap?'
    map_url = (str(endpoint) + 'center=' + str(center_0_http) + '&zoom=' +
               str(self.zoom_level) + '&size=' + str(width) + 'x' + str(height) +
               '&maptype=' + str(self.map_type) + '&key=' + str(self.gapi))
    map_img = Image.open(urlopen(map_url))
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.imshow(map_img, extent=[west, east, south, north], aspect='auto')
    ax.grid(grid)
    plt.show
