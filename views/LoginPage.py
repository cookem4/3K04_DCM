import tkinter as tk
from views import MainPage
from views import NewUserPage
from views.AppFrameBase import AppFrameBase
from services.UserService import UserService


class LoginPage(AppFrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.xPadding = 325
        
        self.welcomeText = tk.Label(self, bg="black",
                                    text="Welcome to the Pacemaker DCM\n This tool allows a pacemaker to be configured in the \n AOO, VOO, AAI, and VVI pacing modes")
        self.welcomeText.config(font=("Helvetica", 20), foreground="white")
        self.welcomeText.grid(row=0, column=0, columnspan=2, padx=(self.xPadding, 0), pady=(200, 75), sticky=tk.N)

        self.badLoginText = tk.Label(self, bg="black", text="INCORRECT USERNAME OR PASSWORD")
        self.badLoginText.configure(font=(50), foreground="red")

        self.userName = tk.Label(self, bg="black", text="Username:")
        self.userName.config(font=(25), foreground="white")
        self.userName.grid(row=1, column=0, padx=(self.xPadding, 0), pady=(20, 0), sticky=tk.E)

        self.passsord = tk.Label(self, bg="black", text="Password:")
        self.passsord.config(font=(25), foreground="white")
        self.passsord.grid(row=2, column=0, padx=(self.xPadding, 0), pady=(20, 0), sticky=tk.E)

        self.usernameEntry = tk.Entry(self, width=20, bg="white", font=(25))
        self.usernameEntry.grid(row=1, column=1, pady=(0, 0), padx=(0, 0), sticky=tk.SW)

        self.passwordEntry = tk.Entry(self, width=20, bg="white", font=(25))
        self.passwordEntry.grid(row=2, column=1, pady=(0, 0), padx=(0, 0), sticky=tk.SW)

        self.loginButton = tk.Button(self, text="Login", width=10, command=self.loginBtn)
        self.loginButton.grid(row=3, column=0, columnspan=2, pady=(25, 0), padx=(self.xPadding, 0), sticky=tk.N)

        self.newAccountButton = tk.Button(self, text="Create New Account", width=20,
                                          command=lambda: parent.switch_frame(NewUserPage.NewUserPage))
        self.newAccountButton.grid(row=4, column=0, columnspan=2, pady=(25, 0), padx=(self.xPadding, 0), sticky=tk.N)

    def loginBtn(self):
        us = UserService()
        username =  self.usernameEntry.get()
        #Save username to text storage for later access
        f = open("currUser.txt", "w+")
        f.write(username)
        f.close()
        password =  self.passwordEntry.get()
        if (us.verify_user(username, password)):
            self.parent.switch_frame(MainPage.MainPage)
        else:
            self.badLoginText.grid(row=0, column=0, columnspan=2, padx=(self.xPadding, 0), pady=(325, 0), sticky=tk.N)
