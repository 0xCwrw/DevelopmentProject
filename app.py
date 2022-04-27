import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from numpy import roots


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
                tk.messagebox.showinfo("Login Successful", "Welcome {}".format(username))
                root.deiconify()
                top.destroy()
            else:
                tk.messagebox.showerror("Information", "The username or password you have entered are incorrect ")
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

        main_frame = tk.Frame(self, bg="#3F6BAA", height=150, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("250x150")
        self.resizable(0, 0)

        self.title("Registration")

        label_user = tk.Label(main_frame, text="New Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(main_frame, text="New Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(main_frame, width=20, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(main_frame, width=20, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(main_frame, text="Create Account", command=lambda: signup())
        button.grid(row=4, column=1)
    
        def signup():
            user = entry_user.get()
            pw = entry_pw.get()
            validation = validate_user(user)
            if not validation:
                tk.messagebox.showerror("information", "Username already exists")
            else:
                if len(pw) > 3:
                    credentials = open("credentials.txt", "a")
                    credentials.write(f"Username,{user},Password,{pw},\n")
                    credentials.close()
                    tk.messagebox.showinfo("Information", "Your account details have been stored.")
                    SignupPage.destroy(self)
                else:
                    tk.messagebox.showerror("information", "Your password is too short")
        def validate_user(username):
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
class MyApp(tk.Tk): # no idea what to put here

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        ttk.Label(self, text="Hello you are in my app").pack()

top = LoginPage()
top.title("Face recognition app - Login")


root = MyApp()
root.withdraw()
root.title("Main page, rename at bottom of script.")
root.mainloop()