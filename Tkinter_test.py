import tkinter

parkFinal = ""
monthFinal = ""
finalFinal = 0
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def submitData():
    print("Information submitted!")
    print(str(parkFinal))
    print(str(finalFinal))
    testRide()
    quit()
def getPark(value):
    global parkFinal
    parkFinal = value
def getMonth(value):
    global finalFinal
    for i in range(12):
        if(months[i] == value):
            finalFinal = i+1
def testRide():
    if parkShow.get() == "mk":
        print(1)
    elif parkShow.get() == "epcot":
        print(2)
    elif parkShow.get() == "hws":
        print(3)

root = tkinter.Tk()
root.title("Fastpass+ Selection")
root.geometry("300x300")

#Create the widgets
submit = tkinter.Button(root, text = "Submit",width=10, command=submitData)

parkShow = tkinter.StringVar(root)
parkShow.set("Park Selection")
park = tkinter.OptionMenu(root, parkShow, "mk", "epcot", "hws", "ak", command=getPark)

monthShow = tkinter.StringVar(root)
monthShow.set("Month Selection")
month = tkinter.OptionMenu(root, monthShow, *months, command=getMonth)

rideShow = tkinter.StringVar(root)
rideShow.set("Ride Selection")
rides = tkinter.OptionMenu(root, rideShow, "test", "test2")

#Place the widgets
submit.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")
park.place(x=10.0,y=10.0)
rides.place(x=10.0,y=40.0)
month.place(x=130.0,y=10.0)
root.mainloop()


