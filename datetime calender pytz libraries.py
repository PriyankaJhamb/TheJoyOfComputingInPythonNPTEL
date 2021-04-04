# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 11:36:28 2021

@author: DELL
"""

from datetime import datetime as dt

import calendar as cd
import pytz #py time zone
import time
print('dt.now():',dt.now())
print('time.time():',time.time())#returns the current time in milli seconds since midnight Jan 1, 1970
tz=pytz.timezone('Singapore')
print(tz)
print(dt.now(tz))
print('pytz.all_timezones:',pytz.all_timezones)

#India -- Asia/Kolkata -- GMT(Greenwith mean time)+5:30
print('len(pytz.all_timezones):',len(pytz.all_timezones))

print('cd.weekday(2001,07,25):',cd.weekday(2001,7,25))
