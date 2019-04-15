# iOS environment
import unittest
from appium import webdriver
import os

desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '11.4'
desired_caps['automationName'] = 'xcuitest'
desired_caps['deviceName'] = 'iPhone Simulator'
desired_caps['app'] = os.path.abspath(r'C:\Users\Cooper\Desktop\DisneyWorld\Payload\WDW.app')

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)