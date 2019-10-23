import tkinter as tk

from exceptions.MaxUsersExceededException import MaxUsersExceededException
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

        self.password = tk.Label(self, bg="black", text="Password:")
        self.password.config(font=(25), foreground="white")
        self.password.grid(row=2, column=0, padx=(self.xPadding, 0), pady=(20, 0), sticky=tk.E)

        self.password = tk.Label(self, bg="black", text="Confirm Password:")
        self.password.config(font=(25), foreground="white")
        self.password.grid(row=3, column=0, padx=(self.xPadding, 0), pady=(20, 0), sticky=tk.E)

        self.usernameEntry = tk.Entry(self, width=20, bg="white", font=(25))
        self.usernameEntry.grid(row=1, column=1, pady=(0, 0), padx=(0, 0), sticky=tk.SW)

        self.passwordEntry = tk.Entry(self, width=20, bg="white", show="*", font=(25))
        self.passwordEntry.grid(row=2, column=1, pady=(0, 0), padx=(0, 0), sticky=tk.SW)

        self.confirmPassword = tk.Entry(self, width=20, bg="white", show="*", font=(25))
        self.confirmPassword.grid(row=3, column=1, pady=(0, 0), padx=(0, 0), sticky=tk.SW)

        self.newAccountButton = tk.Button(self, text="Register", width=20, command=self.register_user)
        self.newAccountButton.grid(row=4, column=0, columnspan=2, pady=(50, 0), padx=(self.xPadding, 0), sticky=tk.N)

        self.backBtn = tk.Button(self, text="Back", width=8, height=1, command=self.go_back)
        self.backBtn.config(font=("Helvetica", 12))
        self.backBtn.grid(row=5, column=0, columnspan=1, pady=(140, 0), padx=(10, 0), sticky=tk.W)

    def go_back(self):
        self.parent.switch_frame(LoginPage.LoginPage)

    def register_user(self):
        new_user_name = self.usernameEntry.get()
        password1 = self.passwordEntry.get()
        password2 = self.confirmPassword.get()

        is_valid_entry = new_user_name != "" and password1 != "" and password1 == password2
        user_exists = self.user_service.exists(new_user_name)

        if is_valid_entry:
            if user_exists:
                self.bad_login_text = tk.Label(self, bg="black", text="      Username Already Exists!      ")
                self.bad_login_text.configure(font=50, foreground="red")
                self.bad_login_text.grid(row=0, column=0, columnspan=2, padx=(self.xPadding, 0), pady=(275, 0),
                                         sticky=tk.N)
            else:
                try:
                    self.user_service.create_by_username_and_password(new_user_name, password1)
                    self.parent.switch_frame(LoginPage.LoginPage)
                except MaxUsersExceededException as e:
                    print(e)
                    self.bad_login_text = tk.Label(self, bg="black", text="Max Number of Users Created")
                    self.bad_login_text.configure(font=(50), foreground="red")
                    self.bad_login_text.grid(row=0, column=0, columnspan=2, padx=(self.xPadding, 0), pady=(275, 0),
                                             sticky=tk.N)

        else:
            self.bad_login_text = tk.Label(self, bg="black", text="         INVALID ENTRY         ")
            self.bad_login_text.configure(font=50, foreground="red")
            self.bad_login_text.grid(row=0, column=0, columnspan=2, padx=(self.xPadding, 0), pady=(275, 0),
                                     sticky=tk.N)
