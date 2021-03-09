# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:44:24 2021

@author: DELL
"""

from gmplot import gmplot
import csv

#place map
gmap=gmplot.GoogleMapPlotter(28,45,17)
#icon
gmap.coloricon="http://www.googlemapsmarkers.com/v1/%s/"

with open("route.csv","r") as f:
    reader=csv.reader(f)
    k=0
    for row in reader:
        lat=float(row[0])
        long=float(row[1])
    if k==0:
        gmap.marker(lat,long,'Yellow')
        k=1
    else:
        gmap.marker(lat, long, 'blue')
    gmap.marker(lat, long, 'red')
    gmap.draw("mymap.html")