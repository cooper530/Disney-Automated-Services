import time
import pyautogui
import keyboard
import calendar
from selenium import webdriver
from selenium import common
import datetime

d = datetime.date.today()
current_month = d.month
password = "mmc4four"

def click_locate(image):
    location = pyautogui.locateCenterOnScreen("Images/" + image)
    pyautogui.click(location)

'''
#INPUTS
month = int(input("Enter desired month (numerical form): "))
day = int(input("Enter desired day (numerical form): "))
park = input("Enter park (mk, epcot, ak, hws): ")
ride = input("Enter ride specified: ")
month_click = month - current_month
'''
month = 4
day = 3
park = "hws"
ride = "rock_and_roller_coaster"

month_click = month - current_month
#Finds what day of the week the day is
week_day = datetime.date(2019, month, day).isoweekday()


driver = webdriver.Chrome()
#What website to access
driver.get("https://disneyworld.disney.go.com/fastpass-plus/select-party/")
driver.maximize_window()

#Finds elements by key
username = driver.find_element_by_name("username")
pswd = driver.find_element_by_name("password")
submit = driver.find_element_by_name("submit")

#Enter the keys
username.send_keys("mmc.4@comcast.net")
pswd.send_keys(password)
submit.click()
time.sleep(5)
try:
    #Select Party Page
    pyautogui.click(366, 531)
    time.sleep(1)
    click_locate("next.PNG")
    time.sleep(2)

    #Month Screen
    for i in range(month_click):
        click_locate("front_arrow.PNG")
    time.sleep(.5)
    click_locate(str(day) + ".PNG")

    #Park Screen
    time.sleep(2.25)
    pyautogui.scroll(-500)
    time.sleep(.5)
    click_locate(str(park) + ".PNG")
    time.sleep(2)

    #Ride screen
    pyautogui.scroll(-100)
    for i in range(4):
        time.sleep(2)
        pyautogui.scroll(-1000)
        try:
            click_locate(str(ride) + ".PNG")
        except TypeError:
            print ("Did not find ride, trying again...")
#except common.exceptions.WebDriverException:
    #print("Web Browser was closed unexpectedly!")
    driver.close()
except TypeError:
    print("Image not found!")
    driver.close()

