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



from selenium import webdriver

print("start....\n")
driver = webdriver.PhantomJS()
driver.get('www.baidu.com/')
print("ok!\n")

