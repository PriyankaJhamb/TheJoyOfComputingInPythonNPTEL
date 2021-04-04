# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:55:59 2021

@author: DELL
"""

from datetime import datetime as dt
import pytz
timezones=pytz.all_timezones
for i in range(len(timezones)):
    zone=timezones[i]
    #create object
    tz=pytz.timezone(zone)
    print("Current time at zone:",zone, "is", dt.now(tz))