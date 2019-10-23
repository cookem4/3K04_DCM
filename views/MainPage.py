import json
import tkinter as tk

from services.UserService import UserService
from views import LoginPage
from views import PacingConfigPage
from views.AppFrameBase import AppFrameBase


class MainPage(AppFrameBase):
    def __init__(self, parent):
        super().__init__(parent)

        self.username = self.session_service.get_current_user()

        self.us = UserService()
        # Obtains current json data for users
        userJson = self.us.getJSON()
        loaded_json = json.loads(userJson)
        for item in loaded_json:
            if (item == self.username):
                self.currUserJson = loaded_json[item]

        self.connectionStateText = tk.Label(self, bg="gray", text="Connection Not Established")
        self.connectionStateText.config(font=("Helvetica", 25), foreground="white")
        self.connectionStateText.grid(row=0, column=0, columnspan=4, padx=(0, 0), pady=(20, 0), sticky=tk.N)

        self.screenInfo = tk.Label(self, bg="light gray", text="HOME", width=48)
        self.screenInfo.config(font=("Helvetica", 35), foreground="black")
        self.screenInfo.grid(row=1, column=0, columnspan=3, padx=(0, 0), pady=(20, 0), sticky=tk.N)

        self.editPacingButton = tk.Button(self, text="Edit Pacing Mode\nand Parameters", width=20, height=6,
                                          command=self.editPacingModes)
        self.editPacingButton.config(font=("Helvetica", 20))
        self.editPacingButton.grid(row=5, column=0, columnspan=3, pady=(50, 0), padx=(45, 0), sticky=tk.NW)

        self.viewCurrEGM = tk.Button(self, text="View Current EGM\nData", width=20, height=6,
                                     command=self.viewCurrEGMDat)
        self.viewCurrEGM.config(font=("Helvetica", 20))
        self.viewCurrEGM.grid(row=5, column=0, columnspan=3, pady=(50, 0), padx=(0, 0), sticky=tk.N)

        self.viewPastEGM = tk.Button(self, text="View Past EGM\nData", width=20, height=6, command=self.viewPastEGMDat)
        self.viewPastEGM.config(font=("Helvetica", 20))
        self.viewPastEGM.grid(row=5, column=0, columnspan=3, pady=(50, 0), padx=(0, 60), sticky=tk.NE)

        self.logoutBtn = tk.Button(self, text="Logout", width=12, height=2, command=self.logout)
        self.logoutBtn.config(font=("Helvetica", 12))
        self.logoutBtn.grid(row=6, column=0, columnspan=1, pady=(125, 0), padx=(10, 0), sticky=tk.W)

        #########################################
        # The following show device information###
        #########################################

        self.programmedModeLabel = tk.Label(self, bg="black",
                                            text="Current Programmed Pacing Mode: " + self.currUserJson[
                                                "pacing_mode_name"])
        self.programmedModeLabel.config(font=(15), foreground="white")
        self.programmedModeLabel.grid(row=2, column=0, columnspan=3, padx=(0, 0), pady=(30, 0), sticky=tk.N)

        self.currIDLabel = tk.Label(self, bg="black", text="Connected Device ID: 123456")
        self.currIDLabel.config(font=(15), foreground="white")
        self.currIDLabel.grid(row=3, column=0, columnspan=3, padx=(0, 0), pady=(0, 0), sticky=tk.N)

        self.prevIDLabel = tk.Label(self, bg="black", text="Previous Device ID: 654321")
        self.prevIDLabel.config(font=(15), foreground="white")
        self.prevIDLabel.grid(row=4, column=0, columnspan=3, padx=(0, 0), pady=(0, 0), sticky=tk.N)

    def editPacingModes(self):
        self.parent.switch_frame(PacingConfigPage.PacingConfigPage)

    def viewCurrEGMDat(self):
        print("Present Data")

    def viewPastEGMDat(self):
        print("Past Data")

    def logout(self):
        self.session_service.invalidate_session()
        self.parent.switch_frame(LoginPage.LoginPage)
