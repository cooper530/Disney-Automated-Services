import tkinter

#Global vars
month = 0
day = 0
park = ""
ride = ""
input_time = ''
grace_period = 0
cycle_time = 0
user_input = ""
password = ""

#DO NOT EDIT THESE LISTS
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days_30 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
days_31 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
days_28 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
times_list = [""]
rides_mk = ["Big Thunder Mountain Railroad", "Buzz Lightyear's Space Ranger Spin", "Barnstormer", "Dumbo", "Enchanted Tales with Belle", "Haunted Mansion", "it's a small world", "Jungle Cruise", "Mad Tea Party","Magic Carpets of Aladdin","The Many Adventures of Winnie the Pooh","Meet Ariel at Her Grotto","Meet Cinderella and Elena at Princess Fairytale Hall","Meet Mickey at Town Square Theater","Meet Rapunzel and Tiana at Princess Fairytale Hall","Meet Tinker Bell at Town Square Theater","Monsters, Inc. Laugh Floor","Peter Pan's Flight","Mickey's PhilharMagic","Pirates of the Caribbean","Seven Dwarfs Mine Train","Space Mountain","Splash Mountain","Tomorrowland Speedway","Under the Sea - Journey of the Little Mermaid"]
rides_epcot = ["Disney & Pixar Short Film Festival","Frozen Ever After","IllumiNations: Reflections of Earth","Journey Into Imagination With Figment","Living with the Land","Meet Disney Pals at the Epcot Character Spot","Mission: SPACE","The Seas with Nemo & Friends","Soarin'","Spaceship Earth","Test Track","Turtle Talk with Crush"]
rides_hws = ["Alien Swirling Saucers","Beauty and the Beast - Live on Stage","Disney Junior Dance Party!","Fantasmic!","For the First Time In Forever: A Frozen Sing-Along Celebration","Indiana Jones Epic Stunt Spectacular!","Muppet*Vision 3D","Rock 'n' Roller Coaster Starring Aerosmith","Slinky Dog Dash","Star Tours: The Adventures Continue","Toy Story Mania!","The Twilight Zone Tower of Terror","Voyage of the Little Mermaid"]
rides_ak = ["Avatar Flight of Passage","DINOSAUR","Expedition Everest - Legend of the Forbidden Mountain","Festival of the Lion King","Finding Nemo - The Musical","It's Tough to Be a Bug!","Kali River Rapids","Kilimanjaro Safaris","Meet Favorite Disney Pals at Adventurers Outpost","Na'vi River Journey","Primeval Whirl","Rivers of Light","UP! A Great Bird Adventure"]

def submitData():
    global month
    global day
    global park
    global ride
    global input_time
    global grace_period
    global cycle_time
    global rideSelect
    global user_input
    global password

    if park == "mk" or park == "epcot" or park == "hws" or park == "ak":
        properTime(hourSelect.get(), minuteSelect.get(), todSelect.get())

    if park == "" or ride == "" or month == 0 or input_time == "Error!" or day == 0:
        popupmsg()

    else:
        print("Information submitted!")
        #print(park)
        #print(ride)
        #print(month)
        #print(day)
        user_input = str(userEntry.get())
        password = str(passwordEntry.get())
        input_time = convert_to_24(input_time)
        (h, m) = input_time.split(':')
        input_time = int(h) * 60 + int(m)

        cycle_time = int(cycleEntry.get())

        #print(cycle_time)
        if graceEntry.get() == "No Period":
            grace_period = 1440
        elif graceEntry.get() == "Exact Time":
            grace_period = 0
        else:
            grace_period = int(graceEntry.get())
        #print(grace_period)
        root.destroy()
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
def selectionClose():
    selection.destroy()
def getDate(value):
    global month
    dayShow = tkinter.StringVar(root)
    dayShow.set("Day Selection")
    for i in range(12):
        if(months[i] == value):
            month = i+1
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        daySelect = tkinter.OptionMenu(root, dayShow, *days_31, command=getDay)
    elif month == 2:
        daySelect = tkinter.OptionMenu(root, dayShow, *days_28, command=getDay)
    else:
        daySelect = tkinter.OptionMenu(root, dayShow, *days_30, command=getDay)

    daySelect.place(x=160.0, y=40.0)
def getDay(value):
    global day
    day = value
def getRide(value):
    global ride
    ride = value
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

def testRide(value):
    global park
    global hourSelect
    global minuteSelect
    global todSelect
    park = value
    rideSelectShow = tkinter.StringVar(root)
    rideSelectShow.set("Ride Selection")

    hourSelect = tkinter.Spinbox(root, from_=1, to=12, width=5)
    minuteSelect = tkinter.Spinbox(root, from_=1, to=59, width=5)
    todSelect = tkinter.Spinbox(root,values= ("AM","PM"), width=5)

    if park == "mk":
        rideSelect = tkinter.OptionMenu(root, rideSelectShow, *rides_mk, command=getRide)
    elif park == "epcot":
        rideSelect = tkinter.OptionMenu(root, rideSelectShow, *rides_epcot, command=getRide)
    elif park == "hws":
        rideSelect = tkinter.OptionMenu(root, rideSelectShow, *rides_hws, command=getRide)
    elif park == "ak":
        rideSelect = tkinter.OptionMenu(root, rideSelectShow, *rides_ak, command=getRide)

    hourSelect.pack_forget()
    minuteSelect.pack_forget()
    rideSelect.pack_forget()
    rideSelect.place(x=10.0, y=70.0)
    hourSelect.place(x=10.0, y=45.0)
    minuteSelect.place(x=60.0, y=45.0)
    todSelect.place(x=110.0, y=45.0)

selection = tkinter.Tk()
selection.title("Fastpass+ Selection")
submitB = tkinter.Button(selection, text = "Submit",width=10, command=selectionClose)
submitB.pack()
var = tkinter.IntVar()
R1 = tkinter.Radiobutton(selection, text="From other python file", variable=var, value=1)
R1.pack(anchor = "w" )
R2 = tkinter.Radiobutton(selection, text="From GUI Interface", variable=var, value=2)
R2.pack(anchor = "w" )
selection.mainloop()

if var.get() == 1:
    print("Launching browser...")
    mode = 1
else:
    mode = 2
    root = tkinter.Tk()
    root.title("Fastpass+ Selection")
    root.geometry("300x300")

    #Create the widgets
    submit = tkinter.Button(root, text = "Submit",width=10, command=submitData)

    parkShow = tkinter.StringVar(root)
    parkShow.set("Park Selection")
    park = tkinter.OptionMenu(root, parkShow, "mk", "epcot", "hws", "ak", command=testRide)

    monthShow = tkinter.StringVar(root)
    monthShow.set("Month Selection")
    month = tkinter.OptionMenu(root, monthShow, *months, command=getDate)

    cycleLabel = tkinter.Label(root, text="Cycle Times:")
    cycleEntry = tkinter.Entry(root, width=5)

    userLabel = tkinter.Label(root, text="Username:")
    userEntry = tkinter.Entry(root)

    passwordLabel = tkinter.Label(root, text="Password:")
    passwordEntry = tkinter.Entry(root, show="*")

    graceLabel = tkinter.Label(root, text="Grace Period:")
    graceEntry = tkinter.Spinbox(root, values=("Exact Time","No Period",5,10,15,20,25,30,35,40,45,50,55,60), width=10)

    #Place the widgets

    submit.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")
    park.place(x=10.0,y=10.0)
    month.place(x=160.0,y=10.0)

    graceLabel.place(x=10,y=250)
    graceEntry.place(x=90,y=250)
    cycleLabel.place(x=10,y=280)
    cycleEntry.place(x=90,y=280)

    userLabel.place(x=10, y=150)
    userEntry.place(x=90, y=150)
    passwordLabel.place(x=10, y=180)
    passwordEntry.place(x=90, y=180)
    root.mainloop()



