#Changes Fastpass to a designated time.

import time
from selenium import webdriver, common
from bisect import bisect_left

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

#Input

#HARD CODED FOR AUGUST TRIP, CHANGE LATER
#user_input = input("Username: ")
#password = input("Password: ")

user_input = "mmc.4@comcast.net"
password = "mmc4four"

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
for i in range(10):
    print(i + 1)
    time.sleep(1)


#View details and modify section
try:
    print("Modifying...")
    modify = driver.find_element_by_css_selector("div.icon.edit.ng-scope.large")
    modify.click()
    time.sleep(1)
    select_all_modify = driver.find_element_by_css_selector("div.link.selectAll.clickable.ng-isolate-scope")
    next_modify = driver.find_element_by_css_selector("div.ng-scope.button.next.primary")
    select_all_modify.click()
    next_modify.click()
    time.sleep(5)
    #Finding ride times again
    view_more_times = driver.find_element_by_css_selector("div.clickable.ng-isolate-scope")
    print(get_text_excluding_children(driver, view_more_times))
    view_more_times.click()
    time.sleep(3)
except common.exceptions.NoSuchElementException:
    print("You did not click a Fastpass+ Selection in time!")
    driver.close()