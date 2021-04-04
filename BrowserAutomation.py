# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 07:43:26 2021

@author: DELL
"""

from selenium import webdriver
#initialisation of web browser
browser=webdriver.Chrome("chromedriver.exe")
browser.get("https://chromedriver.chromium.org/")
# find the xpath by right click on html code line and then click on copy and then Copy Xpath
elem=browser.find_element_by_xpath('//*[@id="COMP_7221429159399122"]/div/ul/li[3]/div/a')
elem.click()
#elements are in div tag
search=browser.find_element_by_id('jot-ui-searchInput')
search.send_keys('Downloads')