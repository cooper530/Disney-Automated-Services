#Changes Fastpass to a designated time.

import time
import tkinter
from selenium import webdriver, common
from bisect import bisect_left

month = 0
day = 0
input_time = ''
user_input = ""
password = ""

def convert_to_24(time):
    """Converts 12 hours time format to 24 hours
    """
    time = time.replace(' ', '')
    time, half_day = time[:-2], time[-2:].lower()
    if half_day == 'am':
        return time
    elif half_day == 'pm':
        split = time.find(':')
        if split == -1:
            split = None
        return str(int(time[:split]) + 12) + time[split:]
    else:
        raise ValueError("Didn't finish with AM or PM.")

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
def popupmsg():
    global popup
    popup = tkinter.Tk()
    popup.wm_title("Error!")
    label = tkinter.Label(popup, text="Please enter all specified information!")
    label.pack(side="top", fill="x", pady=10)
    B1 = tkinter.Button(popup, text="Okay",command=buttonClose)
    B1.pack()
    popup.mainloop()
def buttonClose():
    popup.destroy()
def confirmTime():
    confirm_selection = driver.find_element_by_css_selector("div.ng-scope.button.confirm.tertiary")
    confirm_selection.click()
def properTime(hour, minute, tod):
    global input_time
    if int(hour) > 12 or int(minute) > 59:
        input_time = "Error!"
        return input_time
    else:
        if 0 < int(minute) < 10:
            input_time = hour + ":" + "0" + minute + tod
        else:
            input_time = hour + ":" + minute + tod
        return input_time
def submitData():
    global input_time
    global cycle_time
    global user_input
    global password

    input_time = properTime(hourSelect.get(), minuteSelect.get(), todSelect.get())
    cycle_time = int(cycleEntry.get())
    user_input = str(userEntry.get())
    password = str(passwordEntry.get())

    #print(input_time)
    if input_time == "Error!":
        popupmsg()
    else:
        root.destroy()

#Input
root = tkinter.Tk()
root.title("Fastpass+ Modifier")
root.geometry("300x300")

submit = tkinter.Button(root, text = "Submit",width=10, command=submitData)

cycleLabel = tkinter.Label(root, text="Cycle Times:")
cycleEntry = tkinter.Entry(root, width=5)

userLabel = tkinter.Label(root, text="Username:")
userEntry = tkinter.Entry(root)

passwordLabel = tkinter.Label(root, text="Password:")
passwordEntry = tkinter.Entry(root, show="*")

infoLabel = tkinter.Label(root, text="You will have 10 seconds to make your selection")
infoLabel2 = tkinter.Label(root, text="when the program reaches the Fastpass+ screen.")
submit.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")
cycleLabel.place(x=10,y=280)
cycleEntry.place(x=90,y=280)

infoLabel.place(x=10,y=190)
infoLabel2.place(x=10,y=210)

hourSelect = tkinter.Spinbox(root, from_=1, to=12, width=5)
minuteSelect = tkinter.Spinbox(root, from_=1, to=59, width=5)
todSelect = tkinter.Spinbox(root,values= ("AM","PM"), width=5)

userLabel.place(x=10, y=120)
userEntry.place(x=90, y=120)
passwordLabel.place(x=10, y=150)
passwordEntry.place(x=90, y=150)
hourSelect.pack_forget()
minuteSelect.pack_forget()
hourSelect.place(x=80.0, y=45.0)
minuteSelect.place(x=130.0, y=45.0)
todSelect.place(x=180.0, y=45.0)

root.mainloop()
#ENDS POPUP WINDOW PROGRAM

input_time = convert_to_24(input_time)
(h, m) = input_time.split(':')
input_time = int(h) * 60 + int(m)



#What website to access
driver = webdriver.Chrome()
driver.get("https://disneyworld.disney.go.com/login/?returnUrl=/fastpass-plus/logged-in/")
#driver.maximize_window()
time.sleep(2)

username = driver.find_element_by_name("username")
pswd = driver.find_element_by_name("password")
submit = driver.find_element_by_name("submit")

#Enter the keys
username.send_keys(user_input)
pswd.send_keys(password)
submit.click()
time.sleep(5)

'''
complete = False
while not complete:
    print("Hi")
    time.sleep(1)
    
    try:
        #Never going to be turned true, only placeholder for except error
        if view.is_selected():
            complete = True
    except common.exceptions.StaleElementReferenceException:
        break
'''

#10 second timer
for i in range(5):
    print(i + 1)
    time.sleep(1)


#View details and modify section
try:
    for j in range(cycle_time):
        time.sleep(5)

        print("Modifying...")
        if j == 0:
            ride = driver.find_element_by_css_selector("h3.ng-binding")
            ride = get_text_excluding_children(driver, ride)
        else:
            ride_reload = driver.find_elements_by_css_selector("h3.ng-binding")
            for a_ride in ride_reload:
                name_actual = get_text_excluding_children(driver, a_ride)
                if name_actual == ride:
                    a_ride.click()
                    print("Attraction Re-Identified")
                    break
            time.sleep(.25)

        modify = driver.find_element_by_css_selector("div.icon.edit.ng-scope.large")
        modify.click()
        time.sleep(1)
        select_all_modify = driver.find_element_by_css_selector("div.link.selectAll.clickable.ng-isolate-scope")
        next_modify = driver.find_element_by_css_selector("div.ng-scope.button.next.primary")
        select_all_modify.click()
        next_modify.click()
        time.sleep(5)
        #Finding ride times again
        ride_type = driver.find_elements_by_css_selector("div.name.ng-binding")
        for a_ride in ride_type:
            name_actual = get_text_excluding_children(driver, a_ride)
            if name_actual == ride:
                a_ride.click()
                print("Attraction Identified")
                break
        time.sleep(3)
        ride_time = driver.find_elements_by_css_selector("span.hour.ng-binding")
        am_or_pm = driver.find_elements_by_css_selector("span.ampm.ng-binding")
        overlapTime = driver.find_elements_by_css_selector("div.availableTime.ng-scope.hasTimeOverlap")
        availableTime = driver.find_elements_by_css_selector("div.availableTime.ng-scope")

        try:
            ride_time_str = list(map(str, ride_time))
            # print(ride_time_str)
            # TIME OF DAYS
            time_of_day = []
            for i in am_or_pm:
                ams_pms = get_text_excluding_children(driver, i)
                time_of_day.append(ams_pms)
            # print(time_of_day)

            # Checks for any times that overlap with other fastpasses
            availableTimeList = []
            for i in availableTime:
                # overlaps = get_text_excluding_children(driver, i)
                availableTimeList.append(i)
            # print(availableTimeList)

            overlapTimeList = []
            for i in overlapTime:
                # overlaps = get_text_excluding_children(driver, i)
                overlapTimeList.append(i)
            # print(overlapTimeList)

            # Compares the two lists and creates a true false list
            ability_list = []
            for element in availableTimeList:
                if element in overlapTimeList:
                    ability_list.append(False)
                else:
                    ability_list.append(True)
            #print(ability_list)

            # Converts all the times into minutes
            ride_time_actual = []
            for i in ride_time:
                converted = get_text_excluding_children(driver, i)
                ride_time_actual.append(converted)
            # print(ride_time_actual)

            # Completes the for loop process, by combining the time of day with the ride times into one final list
            final_times_list = []
            for i in range(len(ride_time)):
                together_time = ride_time_actual[i] + time_of_day[i]
                military = convert_to_24(together_time)
                result = timeConversion(military)
                final_times_list.append(result)
            # print (final_times_list)

            counter = 0
            for i in range(len(ability_list)):
                # print(i)
                if ability_list[i] is False:
                    final_times_list.remove(final_times_list[i - counter])
                    counter += 1
                # print(final_times_list)

            # For loop to test if requested time is found (As input) (or a 5-10 minute grace period)
            for i in range(len(final_times_list)):
                if ((final_times_list[i] == input_time or input_time <= final_times_list[i] <= input_time)):
                    ride_time[i].click()
                    print("Time identified!")
                    time.sleep(1)
                    confirmTime()
                    time.sleep(3)
                    # Ends program
                    driver.close()
                    quit()

            # Finds the closest time to the actual time requested
            close_time = takeClosest(final_times_list, input_time)
            print("Close time: " + str(close_time))
            # print ("Closest time:" + str(close_time))

            # Searches for alternate time
            not_found = False
            for i in range(len(final_times_list)):
                # processed_time <= close_time <= input_time or input_time <= close_time <= processed_time
                if (j == 0):
                    if (final_times_list[i] == close_time):
                        processed_time = final_times_list[i]
                        ride_time[i].click()
                        print("Alternate Time Identified")
                        break
                if (j > 0):
                    if final_times_list[i] == close_time and (
                            processed_time <= close_time <= input_time or input_time <= close_time <= processed_time):
                        processed_time = final_times_list[i]
                        ride_time[i].click()
                        not_found = False
                        print("Alternate Time Identified")
                        break
                    else:
                        not_found = True
                        print("No times were closer to desired time.")
                        driver.back()
                        time.sleep(4)
                        break
            if not_found:
                continue
            time.sleep(4)

            # Confirm Time Selection (DO NOT CHANGE)
            confirmTime()
            time.sleep(3)

        except common.exceptions.NoSuchElementException:
            print("Times are not available!")
            driver.back()
            time.sleep(4)

except common.exceptions.NoSuchElementException:
    print("You did not click a Fastpass+ Selection in time!")
    driver.close()

driver.close()