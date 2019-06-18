import time
from InputWindow import *
if mode == 1:
    from FastpassData import *
from selenium import webdriver, common
import datetime
from bisect import bisect_left

d = datetime.date.today()
current_month = d.month

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
username.send_keys(user_input)
pswd.send_keys(password)
submit.click()
time.sleep(5)

try:
    #Select Party Page
    if not people_pick:
        print("Automatic Selection")
        select_all = driver.find_element_by_css_selector("div.link.selectAll.clickable.ng-isolate-scope")
        select_all.click()
        next = driver.find_element_by_css_selector("div.ng-scope.button.next.primary")
        next.click()
    elif people_pick:
        print("Pick your guests")
        next = driver.find_element_by_css_selector("div.ng-scope.button.next.primary")
        complete = False
        while not complete:
            try:
                #Never going to be turned true, only placeholder for except error
                if next.is_selected():
                    complete = True
            except common.exceptions.StaleElementReferenceException:
                break

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
    time.sleep(3)
    try:
        park_find = driver.find_elements_by_css_selector("div.park.ng-scope")
        if (park == "mk"):
            park_find[0].click()
        elif (park == "epcot"):
            park_find[1].click()
        elif (park == "hws"):
            park_find[2].click()
        elif (park == "ak"):
            park_find[3].click()
    except IndexError:
        print("Date not reachable!")
        driver.close()

    time.sleep(6)

    #BEGIN CYCLE TIME
    for j in range(cycle_time):
        global ride
        print("Beginning analysis")
        # Ride screen
        ride_type = driver.find_elements_by_css_selector("div.name.ng-binding")
        for a_ride in ride_type:
            name_actual = get_text_excluding_children(driver, a_ride)
            if name_actual == ride:
                a_ride.click()
                print ("Attraction Identified")
                break
        time.sleep(3)

        #Find and select the time of the ride
        ride_time = driver.find_elements_by_css_selector("span.hour.ng-binding")
        am_or_pm = driver.find_elements_by_css_selector("span.ampm.ng-binding")
        overlapTime = driver.find_elements_by_css_selector("div.availableTime.ng-scope.hasTimeOverlap")
        availableTime = driver.find_elements_by_css_selector("div.availableTime.ng-scope")

        try:

            ride_time_str = list(map(str, ride_time))
            #print(ride_time_str)
            #TIME OF DAYS
            time_of_day = []
            for i in am_or_pm:
                ams_pms = get_text_excluding_children(driver, i)
                time_of_day.append(ams_pms)
            #print(time_of_day)

            #Checks for any times that overlap with other fastpasses
            availableTimeList = []
            for i in availableTime:
                # overlaps = get_text_excluding_children(driver, i)
                availableTimeList.append(i)
            #print(availableTimeList)

            overlapTimeList = []
            for i in overlapTime:
                #overlaps = get_text_excluding_children(driver, i)
                overlapTimeList.append(i)
            #print(overlapTimeList)

            #Compares the two lists and creates a true false list
            ability_list = []
            for element in availableTimeList:
                if element in overlapTimeList:
                    ability_list.append(False)
                else:
                    ability_list.append(True)
            print(ability_list)

            # Converts all the times into minutes
            ride_time_actual = []
            for i in ride_time:
                converted = get_text_excluding_children(driver, i)
                ride_time_actual.append(converted)
            #print(ride_time_actual)

            #Completes the for loop process, by combining the time of day with the ride times into one final list
            final_times_list = []
            for i in range(len(ride_time)):
                together_time = ride_time_actual[i] + time_of_day[i]
                military = convert_to_24(together_time)
                result = timeConversion(military)
                final_times_list.append(result)
            #print (final_times_list)

            counter = 0
            for i in range(len(ability_list)):
                #print(i)
                if ability_list[i] is False:
                    final_times_list.remove(final_times_list[i - counter])
                    counter += 1
                #print(final_times_list)

            # For loop to test if requested time is found (As input) (or a 5-10 minute grace period)
            for i in range(len(final_times_list)):
                if ((final_times_list[i] == input_time or input_time - grace_period <= final_times_list[i] <= input_time + grace_period)):
                    ride_time[i].click()
                    print("Time identified! " + str(grace_period) + " minute grace period.")
                    time.sleep(1)
                    confirmTime()
                    time.sleep(3)
                    #Ends program
                    driver.close()
                    quit()

            #Finds the closest time to the actual time requested
            close_time = takeClosest(final_times_list, input_time)
            print("Close time: " + str(close_time))
            #print ("Closest time:" + str(close_time))

            # Searches for alternate time
            not_found = False
            for i in range(len(final_times_list)):
                #processed_time <= close_time <= input_time or input_time <= close_time <= processed_time
                if (j==0):
                    if (final_times_list[i] == close_time):
                        processed_time = final_times_list[i]
                        ride_time[i].click()
                        print ("Alternate Time Identified")
                        break
                if (j>0):
                    if final_times_list[i] == close_time and (processed_time <= close_time <= input_time or input_time <= close_time <= processed_time):
                        processed_time = final_times_list[i]
                        ride_time[i].click()
                        not_found = False
                        print ("Alternate Time Identified")
                        break
                    else:
                        not_found = True
                        print("No times were closer to desired time.")
                        driver.back()
                        time.sleep(4)
                        break
            if not_found:
                continue
            time.sleep(1)

            # Confirm Time Selection (DO NOT CHANGE)
            confirmTime()
            time.sleep(3)

            #Modify loop
            if (j == 0):
                no_thanks = driver.find_element_by_css_selector("div.ng-scope.button.next.primary")
                no_thanks.click()
            time.sleep(2)

            #Find the ride from earlier
            '''
            STILL WORKING ON THIS PART
            month_and_year = driver.find_elements_by_css_selector("div.listing.ng-scope")
            may_list = []
            print(month_and_year)
            for i in month_and_year:
                converted_time = get_text_excluding_children(driver, i)
                print(converted_time)
                may_list.append(converted_time)
            print(may_list)
            '''


            #Finds ride from the same day (Need to find same day also)
            ride_reload = driver.find_elements_by_css_selector("h3.ng-binding")
            for a_ride in ride_reload:
                name_actual = get_text_excluding_children(driver, a_ride)
                if name_actual == ride:
                    a_ride.click()
                    print("Attraction Re-Identified")
                    break
            time.sleep(.25)
            #View details and modify section
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
            time.sleep(3)

        #common.exceptions.NoSuchElementException
        except common.exceptions.NoSuchElementException:
            print("Times are not available!")
            driver.back()
            time.sleep(4)

        print("Cycle " + str(j + 1) + "/" + str(cycle_time) + " completed!")
    print("Completed repeating cycle!")

    start_over = driver.find_element_by_css_selector("div.ng-scope.button.startOver.secondary")
    start_over.click()
    time.sleep(3)
    arrival_time = driver.find_elements_by_css_selector("span.time.ng-binding")
    completed = []
    for i in arrival_time:
        converted_arrival_time = get_text_excluding_children(driver, i)
        completed.append(converted_arrival_time)
    driver.close()

#common.exceptions.WebDriverException
except common.exceptions.WebDriverException:
    print("Web Browser was closed unexpectedly!")
    driver.close()