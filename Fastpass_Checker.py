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
def confirmTime():
    confirm_selection = driver.find_element_by_css_selector("div.ng-scope.button.confirm.tertiary")
    confirm_selection.click()

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
time.sleep(2)

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

    #BEGIN CYCLE TIME
    for j in range(cycle_time):
        print("Beginning analysis")
        # Ride screen
        ride_type = driver.find_elements_by_css_selector("div.name.ng-binding")
        for i in ride_type:
            name_actual = get_text_excluding_children(driver, i)
            print(name_actual)
            if name_actual == ride:
                i.click()
                print ("Attraction Identified")
                break
        time.sleep(3)

        #Find and select the time of the ride
        ride_time = driver.find_elements_by_css_selector("span.hour.ng-binding")
        am_or_pm = driver.find_elements_by_css_selector("span.ampm.ng-binding")

        try:

            ride_time_str = list(map(str, ride_time))
            #print(ride_time_str)
            #TIME OF DAYS
            time_of_day = []
            for i in am_or_pm:
                ams_pms = get_text_excluding_children(driver, i)
                time_of_day.append(ams_pms)
            print(time_of_day)

            # Converts all the times into minutes
            ride_time_actual = []
            for i in ride_time:
                converted = get_text_excluding_children(driver, i)
                ride_time_actual.append(converted)
            print(ride_time_actual)
            #Completes the for loop process, by combining the time of day with the ride times into one final list
            final_times_list = []
            for i in range(len(ride_time)):
                together_time = ride_time_actual[i] + time_of_day[i]
                military = convert_to_24(together_time)
                result = timeConversion(military)
                final_times_list.append(result)
            print (final_times_list)

            # For loop to test if requested time is found (As input)
            for i in range(len(final_times_list)):
                if (final_times_list[i] == input_time):
                    ride_time[i].click()
                    print("Exact time identified!")
                    time.sleep(1)
                    confirmTime()
                    time.sleep(5)
                    #Ends program
                    driver.close()
                    quit()

            #Finds the closest time to the actual time requested
            close_time = takeClosest(final_times_list, input_time)
            print("Close time: " + str(close_time))
            #print ("Closest time:" + str(close_time))

            # Searches for alternate time
            for i in range(len(final_times_list)):
                if (final_times_list[i] == close_time):
                    ride_time[i].click()
                    print ("Alternate Time Identified")
                    break
            time.sleep(1)

            # Confirm Time Selection (DO NOT CHANGE)
            confirmTime()
            time.sleep(3)

            #Modify loop
            if j == 0:
                no_thanks = driver.find_element_by_css_selector("div.ng-scope.button.next.primary")
                no_thanks.click()
            time.sleep(2)

            #View details and modify section
            view_details = driver.find_element_by_css_selector("span.link.viewDetailLink.ng-scope")
            view_details.click()
            time.sleep(.5)
            modify = driver.find_element_by_css_selector("div.icon.edit.ng-scope.large")
            modify.click()
            time.sleep(1)
            select_all_modify = driver.find_element_by_css_selector("div.link.selectAll.clickable.ng-isolate-scope")
            next_modify = driver.find_element_by_css_selector("div.ng-scope.button.next.primary")
            select_all_modify.click()
            next_modify.click()
            time.sleep(1)
            #Finding ride times again
            view_more_times = driver.find_element_by_css_selector("div.clickable.ng-isolate-scope")
            view_more_times.click()
            time.sleep(5)

        #common.exceptions.NoSuchElementException
        except common.exceptions.NoSuchElementException:
            print("Time/Element not found!")
            driver.back()
            time.sleep(2)

        print("Cycle " + str(j + 1) + "/" + str(cycle_time) + " completed!")
    print("Completed repeating cycle!")
    driver.close()

#common.exceptions.WebDriverException
except TypeError:
    print("Web Browser was closed unexpectedly!")
    driver.close()