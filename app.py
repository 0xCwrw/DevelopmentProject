from cProfile import label
from tkinter import *
from tkinter import messagebox
import os
# from guiTest import name_collection

root = Tk()
root.title('Facial recognition GUI')
root.geometry("500x350")

def openFaceReg():
    faceReg = Toplevel()
    faceReg.title('Face registration')
    faceReg.geometry("500x350")
    welcome = Label(faceReg, text ="Welcome, please enter name.").pack()

    def name_collection():
        if(any(x.isalpha() for x in player_name.get())
        and all(x.isalpha() or x.isspace() for x in player_name.get())):
            username = player_name.get()
            username = username.lower()
            username = username.replace(" ","-")
            parent_directory = "dataset/"
            path = os.path.join(parent_directory, username)
            if os.path.isdir(path):
                messagebox.showerror("Existing user", "This user is already a part of the system.")
            else:
                os.mkdir(path)
                Label(faceReg, text=f'The directory {username} has been created.').pack()
                #possiblly close this window and open one for image collection?
        else:
            messagebox.showerror("Invalid characters detected.", "Invalid characters in username\n letters and white space only.")

# style this window and change variable names.
    player_name = Entry(faceReg, width=30)
    player_name.pack(pady=30)

    


    Button(faceReg, text="register player", padx=10, pady=5, command= name_collection).pack()
    
    
    




# def faceReg_window():
#     # Standard window formating
#     faceReg = Toplevel()
#     faceReg.title('Face registration')
#     faceReg.geometry("500x350")
#     welcome = Label(faceReg, text="Hi").pack()
#     # face registration window specific
#     user = Entry(faceReg, width=50).pack()

 



# def faceRec_window():
#     # Standard window formating
#     faceRec = Toplevel()
#     faceRec.title("Face recognition")
#     faceRec.geometry("500x350")
#     welcome = Label(faceRec, text="Hi this is face rec").pack()
#     # 



faceReg_button = Button(root, text="Register your face here", command=openFaceReg).pack()
# faceRec_button = Button(root, text="Main face registration program", command=faceRec_window).pack()
# button_quit = Button(root, text="Exit program", command=root.quit).pack()
root.mainloop()