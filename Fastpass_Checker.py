import time
from Fastpass_Information import *
from selenium import webdriver
from selenium import common
import datetime
from bisect import bisect_left

d = datetime.date.today()
current_month = d.month
password = "mmc4four"

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
def takeClosest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
       return after
    else:
       return before
def timeConversion(example):
    (h, m) = example.split(':')
    return int(h) * 60 + int(m)

'''
#INPUTS
month = int(input("Enter desired month (numerical form): "))
day = int(input("Enter desired day (numerical form): "))
park = input("Enter park (mk, epcot, ak, hws): ")
ride = input("Enter ride specified: ")
'''

#Finds what day of the week the day is
month_click = month - current_month

#What website to access
driver = webdriver.Chrome()
driver.get("https://disneyworld.disney.go.com/fastpass-plus/select-party/")
#driver.maximize_window()
time.sleep(1)

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

    date_calender = driver.find_elements_by_css_selector("span.day.ng-binding.ng-scope")
    for i in date_calender:
        date_actual = get_text_excluding_children(driver, i)
        if date_actual == str(day):
            i.click()
            print("Date identified")
            break

    #Park Screen
    time.sleep(2.25)
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
    for j in range(cycle_time):
        ride_type = driver.find_elements_by_css_selector("div.name.ng-binding")
        for i in ride_type:
            name_actual = get_text_excluding_children(driver, i)
            if name_actual == ride:
                i.click()
                print ("Attraction Identified")
                break
        time.sleep(3)

        #Find and select the time of the ride
        ride_time = driver.find_elements_by_css_selector("span.hour.ng-binding")
        try:
            for i in ride_time:
                time_actual = get_text_excluding_children(driver, i)
                if time_actual == input_time:
                    i.click()
                    print ("Time Identified")
                    break
            time.sleep(2)
            ride_time_str = list(map(str,ride_time))
            #print (ride_time_str)

            #Converts all the times into minutes
            ride_time_actual = []\
            #FIND OUT HOW TO FIND AM/PM THROUGH DISNEY SECTION
            for i in ride_time:
                converted = get_text_excluding_children(driver, i)
                converted = converted +
                military = convert_to_24(converted)
                result = timeConversion(military)
                ride_time_actual.append(result)
            #print (ride_time_actual)


            #Finds the closest time to the actual time requested
            close_time = takeClosest(ride_time_actual, input_time)
            print ("Closest time:" + str(close_time))

            # Searches for alternate time
            for i in ride_time:
                time_test = get_text_excluding_children(driver, i)
                result_time = timeConversion(time_test)
                if (result_time == close_time):
                    i.click()
                    print ("Alternate Time Identified")
                    break
            time.sleep(1)

            # Confirm Time Selection (DO NOT CHANGE)
            confirm_selection = driver.find_element_by_css_selector("div.ng-scope.button.confirm.tertiary")
            confirm_selection.click()
            time.sleep(5)
        #
        except common.exceptions.NoSuchElementException:
            print("Time not found!")
            driver.back()
            time.sleep(2)
    print("Completed repeating cycle!")
    driver.close()

#common.exceptions.WebDriverException
except common.exceptions.WebDriverException:
    print("Web Browser was closed unexpectedly!")
    driver.close()