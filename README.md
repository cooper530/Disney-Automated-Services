# Disney Automated Services

A collection of automated programs, including the Fastpass+ Checker, Fastpass+ Modifier,
and Disney Reservation Checker by Jmandarino.

### Getting Started

To use all services these libraries must be installed:
* Selenium
* Tkinter
* Twilio
* Python 3.5 or later

## Fastpass+ Checker

### How the Program Works

The Fastpass+ Checker uses the Selenium library to automate the process of Fastpass+ selection.
Information for the requested Fastpass+ can be aquired in two ways. All information for the
variables can be found within FastpassData.py.

#### Method 1:
When prompted, select the GUI interface option to enter information. From there,
use the various drop-down menus and entry fields to enter the information.

#### Method 2:
Instead of using Method 1, select the retrieve data from a python file option.
Enter all information in the FastpassData.py file beforehand to use this method.

## Fastpass+ Modifier

### How the Program Works

The Fastpass+ Modifier uses the same logic as the Fastpass+ Checker, but allows the user to
select an already created Fastpass+ Reservation. Enter the desired time, account information,
and cycle times to run the program. When the browser reaches the Fastpass+ menu,
you will have 10 seconds to choose the Fastpass+ Reservation you wish to modify.
The program will then try to provide you with the closest possible time in the amount of cycles specified.

## Disney Reservation Checker

This program was created by [Jmandarino](https://github.com/Jmandarino). I did not create this program
so all information pertaining to it can be found [here](https://github.com/Jmandarino/Disney-Reservation-Checker)
