import tkinter

parkFinal = ""
monthFinal = 0

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
    print("Information submitted!")
    print(parkFinal)
    print(str(monthFinal))
    quit()
def getDate(value):
    global monthFinal
    dayShow = tkinter.StringVar(root)
    dayShow.set("Day Selection")
    for i in range(12):
        if(months[i] == value):
            monthFinal = i+1
    if monthFinal == 1 or monthFinal == 3 or monthFinal == 5 or monthFinal == 7 or monthFinal == 8 or monthFinal == 10 or monthFinal == 12:
        daySelect = tkinter.OptionMenu(root, dayShow, *days_31)
    elif monthFinal == 2:
        daySelect = tkinter.OptionMenu(root, dayShow, *days_28)
    else:
        daySelect = tkinter.OptionMenu(root, dayShow, *days_30)

    daySelect.place(x=160.0, y=40.0)

def testRide(value):
    global parkFinal
    parkFinal = value
    rideSelectShow = tkinter.StringVar(root)
    rideSelectShow.set("Ride Selection")

    hourSelect = tkinter.Spinbox(root, from_=1, to=12, width=5)
    minuteSelect = tkinter.Spinbox(root, from_=1, to=59, width=5)
    todSelect = tkinter.Spinbox(root,values= ("AM","PM"), width=5)
    if parkFinal == "mk":
        rideSelect = tkinter.OptionMenu(root, rideSelectShow, *rides_mk)
    elif parkFinal == "epcot":
        rideSelect = tkinter.OptionMenu(root, rideSelectShow, *rides_epcot)
    elif parkFinal == "hws":
        rideSelect = tkinter.OptionMenu(root, rideSelectShow, *rides_hws)
    elif parkFinal == "ak":
        rideSelect = tkinter.OptionMenu(root, rideSelectShow, *rides_ak)

    hourSelect.pack_forget()
    minuteSelect.pack_forget()
    rideSelect.pack_forget()
    rideSelect.place(x=10.0, y=70.0)
    hourSelect.place(x=10.0, y=45.0)
    minuteSelect.place(x=60.0, y=45.0)
    todSelect.place(x=110.0, y=45.0)

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

#Place the widgets
submit.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")
park.place(x=10.0,y=10.0)
month.place(x=160.0,y=10.0)
root.mainloop()



