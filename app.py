from tkinter import *
from guiTest import nameit
from face_registration import name_collection

root = Tk()
root.title('Facial recognition GUI')
root.geometry("500x350")

def face_registration_window():
    top = Toplevel()
    top.title('GIVE ME YOUR FACE CHILD GUI')
    top.geometry("400x250")
    lbl = Label(top, text="Hellow world").pack()
    input = Entry(top).pack(pady=20)
    
def face_registration():
    user = name_collection(input.get())
    lbl.config(text=user)

def submit():
    greet = nameit(my_box.get())
    my_label.config(text=greet)


my_box = Entry(root)
my_box.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

my_button = Button(root, text="Submit Name", command=submit)
my_button.pack(pady=20)

face_Button = Button(root, text="GIBE FACE", command=face_registration).pack()
Rec_Button = Button(root, text="Hey ;)", command=face_recognition).pack()

button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()
root.mainloop()