import tkinter as tk
from views import LoginPage
from views.AppFrameBase import AppFrameBase


class NewUserPage(AppFrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.xPadding = 450

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

        self.passwordEntry = tk.Entry(self, width=20, bg="white", font=(25))
        self.passwordEntry.grid(row=2, column=1, pady=(0, 0), padx=(0, 0), sticky=tk.SW)

        self.confirmPassword = tk.Entry(self, width=20, bg="white", font=(25))
        self.confirmPassword.grid(row=3, column=1, pady=(0, 0), padx=(0, 0), sticky=tk.SW)

        self.newAccountButton = tk.Button(self, text="Register", width=20, command=self.registerUser)
        self.newAccountButton.grid(row=4, column=0, columnspan=2, pady=(50, 0), padx=(self.xPadding, 0), sticky=tk.N)

    def registerUser(self):
        self.parent.switch_frame(LoginPage.LoginPage)
