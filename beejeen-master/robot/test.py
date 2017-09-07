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


chars = 'aA09~`! @#$%^&*()-=_+[]\\{}|;\':",./<>?'
length = randint(0, 100)

country = 'Croatia'

if len(sys.argv) == 1:
    fois = 5
else:
    fois = sys.argv[1]

i = 0
waitDuration = 2
driver = webdriver.Chrome()

while i < int(fois):
    if i % 2 == 0:
        msg = ''.join(random.choice(chars) for _ in range(length))
    else:
        msg = country
    try:
        driver.get('http://www.beejeen.com')
        # selenium can only wait for the superlink or the web form
        # so we have to set a duration to let it wait for
        txt = WebDriverWait(driver, waitDuration).until(EC.presence_of_element_located((By.ID, "input-text")))
        #txt = driver.find_element_by_id('input-text')
        txt.clear()
        txt.send_keys(msg)
        btn = driver.find_element_by_id('input-search')
        btn.click()
        #print(driver.page_source.encode('utf-8'))
        countryDescriptionElement = WebDriverWait(driver, waitDuration).until(EC.presence_of_element_located((By.ID, "country-description")))
    except WebDriverException as ex:
        pass
        #print("Enter: " + msg + ", Error: " + str(ex) + ", Found: " + driver.page_source)
    i += 1

driver.quit()
