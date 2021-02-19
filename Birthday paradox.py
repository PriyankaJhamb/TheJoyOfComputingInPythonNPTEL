# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:17:51 2021

@author: DELL
"""
import random
import datetime
def birthday_paradox():
    birthday=[]
    i=0
    while (i<50):
        year=random.randint(1895, 2017)
        #the oldest person ever lived was 122 years old.
        if year%4==0 and year%100!=0 or year%400==0:
            leap=1
        else:
            leap=0
        
        month=random.randint(1,12)
        if(month==2 and leap==1):
            day=random.randint(1,29)
        elif (month==2 and leap==0):
            day=random.randint(1,28)
        elif month==4 or month==6:
            day=random.randint(1,30)
        elif month%2!=0 and month<=7:
            day=random.randint(1,31)
        elif month%2==0 and month>7:
            day=random.randint(1,31)
        else:
            day=random.randint(1,30)
            
        dd=datetime.date(year,month,day)
        day_of_year=dd.timetuple().tm_yday
        print(day_of_year)
        i=i+1
        birthday.append(day_of_year)
        print(dd)
        
    birthday.sort()
    i=0
    while(i<50):
        print(birthday[i])
        i=i+1
    
birthday_paradox()



print("datetime library functions:")
print()

print("Today's date: " ,datetime.date.today())
print("Year: ", datetime.date.today().strftime("%Y"))
print("Month: ",datetime.date.today().strftime("%B"))
print("Day: ", datetime.date.today().strftime("%d"))
print("Week number of the Year: ",datetime.date.today().strftime("%W"))
print("Week day of the week:",datetime.date.today().strftime("%w"))
print("Day of the year: ", datetime.date.today().strftime("%j"))
print("Day of the week: ", datetime.date.today().strftime("%A"))
print("Current date and time: ",datetime.datetime.now())
