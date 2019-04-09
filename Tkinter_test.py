import tkinter

def submitData():
    print("Information submitted!")

root = tkinter.Tk()
root.title("Fastpass+ Selection")
root.geometry("500x500")
submit = tkinter.Button(root, text = "Submit", height=1,width=10, command=submitData)

submit.place(x=400,y=470)
# Code to add widgets will go here...
root.mainloop()


