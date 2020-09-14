#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 01:38:04 2020

@author: shruti
"""

"""
FOR FIREFOX(DO IT ONCE)
!pip install geckodriver_autoinstaller
import geckodriver_autoinstaller
geckodriver_autoinstaller.install()
"""
import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.google.com/");
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('images of dog')
search_box.submit()
time.sleep(5)
driver.quit()


firefox = webdriver.Firefox()
firefox.get("https://www.google.com")
time.sleep(5)
search = firefox.find_element_by_name('q')
search.send_keys('images of food')
search.submit()
time.sleep(5)
firefox.quit()