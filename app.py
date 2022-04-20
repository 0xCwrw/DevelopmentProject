from tkinter import *
root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "enter your name: ")

def myClick():
    hello = "hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="enter name", command=myClick)
myButton.pack()

root.mainloop()