from time import sleep
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import cv2
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
        if(any(x.isalpha() for x in user_name.get())
        and all(x.isalpha() or x.isspace() for x in user_name.get())):
            username = user_name.get()
            username = username.lower()
            username = username.replace(" ","-")
            parent_directory = "dataset/"
            path = os.path.join(parent_directory, username)
            if os.path.isdir(path):
                messagebox.showerror("Existing user", "This user is already a part of the system.")
            else:
                os.mkdir(path)
                Label(faceReg, text=f'The directory {username} has been created.').pack()
                sleep(1)
                image_collection(path)
                #possiblly close this window and open one for image collection?
        else:
            messagebox.showerror("Invalid characters detected.", "Invalid characters in username\n letters and white space only.")

    def image_collection(path):
        face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
        collection_progess = ttk.Progressbar(faceReg, orient=HORIZONTAL, length=300, mode='determinate')
        collection_progess.pack()
        for i in range(1, 4):
            while(True):
                ret, frame = cap.read()
                frame = cv2.flip(frame, 0)
                sleep(1)
                break
            sleep(2)
            while(True):
                # Capture frame-by-frame
                ret, frame = cap.read()
                frame = cv2.flip(frame, 0)
                gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
                if len(faces) == 1:
                    message = f'Face detected, sample {i}/30 successful.'
                    break
                elif len(faces) < 1:
                    message = "No face detected, please adjust."
                else:
                    message = "Too many faces detected, there should only be one person in frame."
            cv2.imwrite("{}/test{}.png".format(path, i), frame)
            sleep(1.6)
            message_label = Label(faceReg, text = message)
            message_label.pack()
            collection_progess['value'] += 33
            faceReg.update_idletasks()
        sleep(2)
        finsih = messagebox.showinfo('User setup complete.','Press OK to finish.')
        if finsih == "ok":
            faceReg.destroy()
    # End of face registration functions.

    # style this window and change variable names.
    user_name = Entry(faceReg, width=30)
    user_name.pack(pady=30)
    Button(faceReg, text="register player", padx=10, pady=5, command= name_collection).pack()

# End of face registration window.
    
    




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