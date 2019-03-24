from twilio.rest import Client
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json
import os
import threading
import time as TIME

driver = webdriver.Chrome()
#What website to access
driver.get("http://www.python.org")

#Confirms website is correct
assert "Python" in driver.title
#Finds elements by key
#elem = driver.find_element_by_name("q")
elem = driver.find_element_by_name("Python Community")
elem.click()
time.sleep(3)
'''
#Searches by certain keys: "pycon" and RETURN key
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

#Checks if nothing was really found
assert "No results found." not in driver.page_source
'''
#Closes browser
driver.close()