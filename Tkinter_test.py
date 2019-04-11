import tkinter
parkFinal = ""
monthFinal = ""

def submitData():
    print("Information submitted!")
    print(str(parkFinal))
    print(str(monthFinal))
    quit()
def getPark(value):
    global parkFinal
    parkFinal = value
def getMonth(value):
    global monthFinal
    monthFinal = value


root = tkinter.Tk()
root.title("Fastpass+ Selection")
root.geometry("300x300")

#Create the widgets
submit = tkinter.Button(root, text = "Submit",width=10, command=submitData)
'''
parkDrop = tkinter.Listbox (root)
parkDrop.insert(1, "Magic Kingdom")
parkDrop.insert(2, "EPCOT")
parkDrop.insert(3, "Hollywood Studios")
parkDrop.insert(4, "Animal Kingdom")
'''
parkShow = tkinter.StringVar(root)
parkShow.set("Park Selection")
park = tkinter.OptionMenu(root, parkShow, "mk", "epcot", "hws", "ak", command=getPark)
monthShow = tkinter.StringVar(root)
monthShow.set("Month Selection")
month = tkinter.OptionMenu(root, monthShow, "March", "April", "May", command=getMonth)
#Place the widgets
submit.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")
park.place(x=10.0,y=10.0)
month.place(x=130.0,y=10.0)
root.mainloop()


