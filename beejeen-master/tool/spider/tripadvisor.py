#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
#-*- coding: UTF-8 -*-


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import sys
import string
import random
from random import randint
import time

from ConnectionDB import ConnectionDB



#btn = driver.find_element_by_class_name('search')
#print(driver.find_elements_by_css_selector('div#ppr_rup.ppr_priv_global_nav.cye-lm-tag'))
#print(driver.page_source.encode('utf-8'))


#conndb = ConnectionDB()

waitDuration = 5


i = 0
try:
    driver = webdriver.Chrome()
    
    driver.get('https://www.tripadvisor.cn/')
    
    btn = WebDriverWait(driver, waitDuration).until(EC.presence_of_element_located((By.CLASS_NAME, "search")))
    btn.click()

    while True:
        txt = WebDriverWait(driver, waitDuration).until(EC.presence_of_element_located((By.ID, "mainSearch")))
        if txt.is_displayed():
            break
    txt.send_keys("契迪龙寺")
    btn = driver.find_element_by_id('SEARCH_BUTTON')
    btn.click()
    btn.click()
    ele = WebDriverWait(driver, waitDuration).until(EC.presence_of_element_located((By.CLASS_NAME, "result_wrap ")))
    ele.click()
    driver.switch_to_window(driver.window_handles[2])
    print(driver.find_element_by_class_name('street-address').text)
    try:
        print(driver.find_element_by_class_name('extended-address').text)
    except:
        pass
    print(driver.find_element_by_class_name('heading_title ').text)

    time.sleep(2)
    driver.quit()
    i += 1
except Exception as e:
    print(e)
    time.sleep(2)
    driver.quit()
