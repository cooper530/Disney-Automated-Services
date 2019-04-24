from selenium import webdriver
from selenium import common
import time

resortDict = {"copper creek": "copper-creek-villas-cabins-disneys-wilderness-lodge"}
resort = input("Enter home resort name: ")

resort = resortDict.get(resort)

driver = webdriver.Chrome()

driver.get("https://www.fidelityresales.com/resort/" + resort)
#driver.find_element_by_class_name()
