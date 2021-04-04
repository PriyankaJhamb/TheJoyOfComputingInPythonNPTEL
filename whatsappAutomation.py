# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 08:27:55 2021

@author: DELL
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("chromedriver.exe")
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,600)
target='"Vrishti CSE GNE"'#Enter your friend's name # don't put space btw ' and "
string="Right [Action, Time, Direction, Energy]"#The message you want to send to your friend
# elements is in span tag
x_arg='//span[contains(@title, '+ target + ')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
#target=wait.until(EC.presence_of_all_elements_located((By.XPATH, x_arg)))#not fetching
target.click()

input_box=driver.find_element_by_class_name('_2A8P4')
for i in range(0,5):
    input_box.send_keys(string+Keys.ENTER)
