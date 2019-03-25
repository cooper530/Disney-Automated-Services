import time
import pyautogui
import keyboard
import calendar
from selenium import webdriver
import datetime

d = datetime.date.today()
current_month = d.month
password = "mmc4four"

'''
1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thursday
5 = Friday
6 = Saturday
7 = Sunday
'''

#INPUTS
month = int(input("Enter desired month (numerical form): "))
day = int(input("Enter desired day (numerical form): "))
month_click = month - current_month

#Finds what day of the week the day is
week_day = datetime.date(2019, month, day).isoweekday()

#Finds what week the day is in (Week 0,1,2,etc.) CAN BE LIST FORM
print (calendar.monthcalendar(2019, month))


driver = webdriver.Chrome()
#What website to access
driver.get("https://disneyworld.disney.go.com/fastpass-plus/select-party/")
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
#Select Party Page
pyautogui.click(152, 707)
time.sleep(.5)
pyautogui.click(1190, 975)
time.sleep(2)
#Month Screen
for i in range(month_click):
    pyautogui.click(821, 352)
time.sleep(3)
if week_day == 1:
    pyautogui.click(315, 480)

print (pyautogui.position())

driver.close()
