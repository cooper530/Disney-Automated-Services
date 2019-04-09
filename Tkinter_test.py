import tkinter
parkFinal = ""
def submitData():
    print("Information submitted!")
    print(str(parkFinal))
    quit()
def getPark(value):
    global parkFinal
    parkFinal = value

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

#Place the widgets
submit.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")
park.place(x=10.0,y=10.0)
root.mainloop()


