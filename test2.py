import time
from selenium import webdriver

password = ""
driver = webdriver.Chrome()
#What website to access
driver.get("https://disneyworld.disney.go.com/fastpass-plus/select-party/")

#Confirms website is correct
assert "Fastpass+ Planning" in driver.title
#Finds elements by key
elem = driver.find_element_by_id("submit")
elem.click()
time.sleep(3)

driver.close()