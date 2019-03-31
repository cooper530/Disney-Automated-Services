from selenium import webdriver
from selenium import common
import time


resort = input("Enter home resort name: ")

if (resort == "copper creek"):
    resort = "copper-creek-villas-cabins-disneys-wilderness-lodge"

driver = webdriver.Chrome()
#
driver.get("https://www.fidelityresales.com/resort/" + resort)
driver.find_element_by_class_name()
