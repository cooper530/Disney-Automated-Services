import tkinter

def submitData():
    print("Information submitted!")
    print(park.get(park.curselection()))
    quit()

root = tkinter.Tk()
root.title("Fastpass+ Selection")
root.geometry("300x300")

#Create the widgets
submit = tkinter.Button(root, text = "Submit",width=10, command=submitData)
park = tkinter.Listbox (root)
park.insert(1, "Magic Kingdom")
park.insert(2, "EPCOT")
park.insert(3, "Hollywood Studios")
park.insert(4, "Animal Kingdom")


#Place the widgets
submit.place(rely=1.0, relx=1.0, x=0, y=0, anchor="se")
park.pack()
root.mainloop()


