import tkinter as tk

from services.UserService import UserService
from views import LoginPage
from views.AppFrameBase import AppFrameBase


class NewUserPage(AppFrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.xPadding = 225

        self.newUserText = tk.Label(self, bg="black", text="Please enter your new username and password")
        self.newUserText.config(font=("Helvetica", 30), foreground="white")
        self.newUserText.grid(row=0, column=0, columnspan=2, padx=(self.xPadding, 0), pady=(200, 75), sticky=tk.N)

        self.userName = tk.Label(self, bg="black", text="Username:")
        self.userName.config(font=(25), foreground="white")
        self.userName.grid(row=1, column=0, padx=(self.xPadding, 0), pady=(0, 0), sticky=tk.E)

        self.passsord = tk.Label(self, bg="black", text="Password:")
        self.passsord.config(font=(25), foreground="white")
        self.passsord.grid(row=2, column=0, padx=(self.xPadding, 0), pady=(20, 0), sticky=tk.E)

        self.passsord = tk.Label(self, bg="black", text="Confirm Password:")
        self.passsord.config(font=(25), foreground="white")
        self.passsord.grid(row=3, column=0, padx=(self.xPadding, 0), pady=(20, 0), sticky=tk.E)

        self.usernameEntry = tk.Entry(self, width=20, bg="white", font=(25))
        self.usernameEntry.grid(row=1, column=1, pady=(0, 0), padx=(0, 0), sticky=tk.SW)

        self.passwordEntry = tk.Entry(self, width=20, bg="white", show="*", font=(25))
        self.passwordEntry.grid(row=2, column=1, pady=(0, 0), padx=(0, 0), sticky=tk.SW)

        self.confirmPassword = tk.Entry(self, width=20, bg="white", show="*", font=(25))
        self.confirmPassword.grid(row=3, column=1, pady=(0, 0), padx=(0, 0), sticky=tk.SW)

        self.newAccountButton = tk.Button(self, text="Register", width=20, command=self.registerUser)
        self.newAccountButton.grid(row=4, column=0, columnspan=2, pady=(50, 0), padx=(self.xPadding, 0), sticky=tk.N)

        self.backBtn = tk.Button(self, text="Back", width=8, height=1, command=self.goBack)
        self.backBtn.config(font=("Helvetica", 12))
        self.backBtn.grid(row=5, column=0, columnspan=1, pady=(140, 0), padx=(10, 0), sticky=tk.W)

    def goBack(self):
        self.parent.switch_frame(LoginPage.LoginPage)

    def registerUser(self):
        us = UserService()
        newUserName = self.usernameEntry.get()
        password1 = self.passwordEntry.get()
        password2 = self.confirmPassword.get()
        if (newUserName != "" and password1 != "" and password1 == password2 and not (us.user_exists(newUserName))):
            try:
                us.create_by_username_and_password(newUserName, password1)
                self.parent.switch_frame(LoginPage.LoginPage)
            except Exception as e:
                print(e)
                self.badLoginText = tk.Label(self, bg="black", text="Max Number of Users Created")
                self.badLoginText.configure(font=(50), foreground="red")
                self.badLoginText.grid(row=0, column=0, columnspan=2, padx=(self.xPadding, 0), pady=(275, 0),
                                       sticky=tk.N)
        else:
            if (newUserName != "" and password1 != "" and password1 == password2 and us.user_exists(newUserName)):
                self.badLoginText = tk.Label(self, bg="black", text="      Username Already Exists!      ")
                self.badLoginText.configure(font=(50), foreground="red")
                self.badLoginText.grid(row=0, column=0, columnspan=2, padx=(self.xPadding, 0), pady=(275, 0),
                                       sticky=tk.N)
            else:
                self.badLoginText = tk.Label(self, bg="black", text="         INVALID ENTRY         ")
                self.badLoginText.configure(font=(50), foreground="red")
                self.badLoginText.grid(row=0, column=0, columnspan=2, padx=(self.xPadding, 0), pady=(275, 0),
                                       sticky=tk.N)
