import tkinter as tk
from tkinter import Label, messagebox
from tkinter import ttk
from numpy import roots
import os
import cv2
from time import sleep
from PIL import Image
import pickle


class LoginPage(tk.Tk): # modify for face recognition instead of pswd, then add if fails to use pswd
    def __init__(self, *args, **kwards):
        tk.Tk.__init__(self, *args, **kwards)
        
        main_frame = tk.Frame(self, bg="#000", height = 431, width=626)
        main_frame.pack(fill="both", expand = "true")

        self.geometry("626x431")
        self.resizable(0,0)

        login_frame = tk.Frame(main_frame, bg="#FFF", relief="groove", bd=2)
        login_frame.place(rely=0.30, relx=0.17, height=130, width=400)
        
        label_title = tk.Label(login_frame, text="Login Page")
        label_title.grid(row=0, column=1, columnspan=1)

        label_user = tk.Label(login_frame, text="Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(login_frame, text="Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(login_frame, width=45, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(login_frame, width=45, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(login_frame, text="Login", command=lambda: getlogin())
        button.place(rely=0.70, relx=0.50)

        signup_btn = ttk.Button(login_frame, text="Register", command=lambda: get_signup())
        signup_btn.place(rely=0.70, relx=0.75)

        def get_signup():
            SignupPage()
        
        def getlogin():
            username = entry_user.get()
            password = entry_pw.get()
            validation = validate(username, password)
            if validation:
                Face_recognition = MFA(username)
                if Face_recognition:
                    tk.messagebox.showinfo("Login Successful", "Welcome {}".format(username))
                    root.deiconify()
                    top.destroy()
            else:
                tk.messagebox.showerror("Information", "The username or password you have entered are incorrect ")

        def MFA(username):
            face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
            recogniser = cv2.face.LBPHFaceRecognizer_create()
            recogniser.read("recognisers/face-trainner.yml")

            labels = {"person_name": 1}
            with open("identities/face-labels.pickle", 'rb') as f:
                og_labels = pickle.load(f)
                labels = {v:k for k,v in og_labels.items()}

            cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
            sleep(0.1)
            detected = 1
            while detected <= 10:
                while(True):
                    # Capture frame-by-frame
                    ret, frame = cap.read()
                    frame = cv2.flip(frame, 0)
                    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
                    for (x, y, w, h) in faces:
                        # print(x,y,w,h)
                        roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
                        roi_color = frame[y:y+h, x:x+w]
                        #After prediction of ROI (Region of interest) computation is focused in that area.
                        id_, conf = recogniser.predict(roi_gray)
                        if conf>=40 and conf <= 80:
                            name = labels[id_]
                            name = name.replace("-", " ")
                            USER = username.lower()
                            if name == USER:
                                print(F'{USER} detected.')
                                detected +=1
                    
                    cv2.imshow('Face detection',frame)
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                    break
            # When everything done, release the capture
            cap.release()
            cv2.destroyAllWindows()
            return True
        def validate(username, password):
            try:
                with open("credentials.txt", "r") as credentials:
                    for line in credentials:
                        line = line.split(",")
                        if line [1] == username and line[3] == password:
                            return True
                    return False
            except FileNotFoundError:
                print("you need to register first")
                return False

class SignupPage(tk.Tk):        # incorporate the face registration process here
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#FFF", height = 431, width=626)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand = "true")
        # pack_propagate prevents the window resizing to match the widgets
        

        self.geometry("450x350")
        self.resizable(0, 0)

        self.title("Registration")
        addUser_frame = tk.Frame(main_frame, bg="#FFF", relief="groove", bd=2)
        addUser_frame.place(rely=0.30, relx=0.17, height=130, width=400)

        label_user = tk.Label(addUser_frame, text="New Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(addUser_frame, text="New Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(addUser_frame, width=20, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(addUser_frame, width=20, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(addUser_frame, text="Create Account", command=lambda: signup())
        button.grid(row=4, column=1)

        display_label = Label(addUser_frame)
        display_label.grid(row=5, column=1)
    
        def signup():
            user = entry_user.get()
            pw = entry_pw.get()
            validation = validate_user(user)
            if not validation:
                tk.messagebox.showerror("information", "Invlid character or username already exists")
            else:
                if len(pw) > 3:
                    credentials = open("credentials.txt", "a")
                    credentials.write(f"Username,{user},Password,{pw},\n")
                    credentials.close()
                    parent_directory = "dataset/"
                    user = user.lower()
                    user = user.replace(" ","-")
                    path = os.path.join(parent_directory, user)
                    if os.path.isdir(path):
                        messagebox.showerror("Existing user", "This user is already a part of the system.")
                    else:
                        os.mkdir(path)
                        tk.messagebox.showinfo("Information", "Your account details have been stored.\nFace registration will now begin.")
                        image_collection(path)
                else:
                    tk.messagebox.showerror("information", "Your password is too short")
        def validate_user(username):
            if(any(x.isalpha() for x in username)
            and all(x.isalpha() or x.isspace() for x in username)):
                # Checks the text file for a username/password combination.
                try:
                    with open("credentials.txt", "r") as credentials:
                        for line in credentials:
                            line = line.split(",")
                            if line[1] == username:
                                return False
                    return True
                except FileNotFoundError:
                    return True
            else:
                return False
        def image_collection(path):
            face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
            cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
            # collection_progess = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode='determinate')
            # collection_progess.pack()
            for i in range(1, 31):
                while(True):
                    # Capture frame-by-frame
                    ret, frame = cap.read()
                    frame = cv2.flip(frame, 0)
                    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
                    message = ""
                    cv2.imshow(f'Face registration: {message}', frame)
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows
                    if len(faces) ==1:
                        message = f'Face detected, sample {i}/30 successful'
                        break
                    elif len(faces) < 1:
                        message = "No faces detected."
                    else:
                        message = "Too many faces detected."
                cv2.imwrite("{}/test{}.png".format(path, i), frame)
                sleep(1.6)
                # message_label = Label(faceReg, text = message)
                # message_label.pack()
                # collection_progess['value'] += 33
                # faceReg.update_idletasks()
            sleep(2)
            cap.release()
            cv2.destroyAllWindows()
            finsih = messagebox.showinfo('User setup complete.','Press OK to finish.')
            exec(open('faces_training.py').read())
            if finsih == "ok":
                SignupPage.destroy(self)    
class MyApp(tk.Tk): # no idea what to put here

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        ttk.Label(self, text="Hello you are in my app").pack()

        self.geometry("626x431")
        self.resizable(0,0)

top = LoginPage()
top.title("Face recognition app - Login")


root = MyApp()
root.withdraw()
root.title("Main page, rename at bottom of script.")
root.mainloop()