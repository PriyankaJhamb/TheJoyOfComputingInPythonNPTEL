# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:37:48 2021

@author: DELL
"""

import calendar as cd
def check_leap(y):
    if y%100==0:
        if y%400==0:
            return True
        else:
            return False
    else:
        if y%4==0:
            return True
        else:
            return False
        
def check_valid_date(d, m, y, l):
    if l:
        if m==2:
            if d<30:
                return True
            else:
                return False
        else:
            if m>8:
                if m%2==1:
                    if d<32:
                        return True
                    else:
                        return False
                else:
                    if d<31:
                        return True
                    else:
                        return False
            else:
                if m%2==0:
                    if d<32:
                        return True
                    else:
                        return False
                else:
                    if d<31:
                        return True
                    else:
                        return False
    else:
        if m==2:
            if d<29:
                return True
            else:
                return False
        else:
            if m>8:
                if m%2==1:
                    if d<32:
                        return True
                    else:
                        return False
                else:
                    if d<31:
                        return True
                    else:
                        return False
            else:
                if m%2==0:
                    if d<32:
                        return True
                    else:
                        return False
                else:
                    if d<31:
                        return True
                    else:
                        return False
                
        
def get_day(day_index):
    list_of_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    return list_of_days[day_index]
            
while(1):
    year=int(input('Enter the day starting from 1970:'))
    if year<1970:
        print('Enter a year starting from 1970:')
    else:
        break
    
while(1):
    month=int(input('Enter month (1-12):'))
    if month<12 and month>0:
        break
    else:
        print('Enter a month in the range(1-12):')
        
leap=check_leap(year)
while(1):
    date=int(input('Enter date:'))
    if date>0 and check_valid_date(date, month, year, leap):
        break
    else:
        print('Enter a valid date:')
        

        
day_index=cd.weekday(year, month, date)
day=get_day(day_index)
print(date, "/", month,"/",year,"falls on", day)
