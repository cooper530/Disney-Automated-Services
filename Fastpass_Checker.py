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
def get_text_excluding_children(driver, element):
    return driver.execute_script("""
    var parent = arguments[0];
    var child = parent.firstChild;
    var ret = "";
    while(child) {
        if (child.nodeType === Node.TEXT_NODE)
            ret += child.textContent;
        child = child.nextSibling;
    }
    return ret;
    """, element)

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
    select_all = driver.find_element_by_css_selector("div.link.selectAll.clickable.ng-isolate-scope")
    select_all.click()
    next = driver.find_element_by_css_selector("div.ng-scope.button.next.primary")
    next.click()
    time.sleep(2)

    #Month Screen
    front_arrow = driver.find_element_by_css_selector("span.next-month")
    for i in range(month_click):
        front_arrow.click()
    time.sleep(.25)
    pyautogui.click(934, 351)
    #click_locate(str(day) + ".PNG")

    #Park Screen
    time.sleep(2)
    park_find = driver.find_elements_by_css_selector("div.park.ng-scope")
    if (park == "mk"):
        park_find[0].click()
    elif (park == "epcot"):
        park_find[1].click()
    elif (park == "hws"):
        park_find[2].click()
    elif (park == "ak"):
        park_find[3].click()
    time.sleep(5)

    #Ride screen
    pyautogui.scroll(-100)
    '''
    for i in range(4):
        time.sleep(2)
        pyautogui.scroll(-1000)
        try:
            click_locate(str(ride) + ".PNG")
        except TypeError:
            print ("Did not find ride, trying again...")
    '''
    ride_type = driver.find_elements_by_css_selector("div.name.ng-binding")
    for i in ride_type:
        name_actual = get_text_excluding_children(driver, ride_type[i])
        print (name_actual)
        '''
        if name_actual == ride:
            ride_type[i].click()
            print ("Found!")
        else:
            print ("Not yet!")
            continue
        '''

except common.exceptions.WebDriverException:
    print("Web Browser was closed unexpectedly!")
    driver.close()