import tkinter as tk

from main.views import PacingConfigPage, LoginPage
from main.views.AppFrameBase import AppFrameBase


class MainPage(AppFrameBase):
    def __init__(self, parent):
        super().__init__(parent)
        username = self.session_service.get().username
        self.currUserJson = self.user_service.read(username).to_json()

        self.connectionStateText = tk.Label(self, bg="gray", text="Connection Not Established")
        self.connectionStateText.config(font=("Helvetica", 25), foreground="white")
        self.connectionStateText.grid(row=0, column=0, columnspan=4, padx=(0, 0), pady=(20, 0), sticky=tk.N)

        self.screenInfo = tk.Label(self, bg="light gray", text="HOME", width=48)
        self.screenInfo.config(font=("Helvetica", 35), foreground="black")
        self.screenInfo.grid(row=1, column=0, columnspan=3, padx=(0, 0), pady=(20, 0), sticky=tk.N)

        self.editPacingButton = tk.Button(self, text="Edit Pacing Mode\nand Parameters", width=20, height=6,
                                          command=self.edit_pacing_modes_callback)
        self.editPacingButton.config(font=("Helvetica", 20))
        self.editPacingButton.grid(row=5, column=0, columnspan=3, pady=(50, 0), padx=(45, 0), sticky=tk.NW)

        self.viewCurrEGM = tk.Button(self, text="View Current EGM\nData", width=20, height=6,
                                     command=self.view_current_EGM_data_callback)
        self.viewCurrEGM.config(font=("Helvetica", 20))
        self.viewCurrEGM.grid(row=5, column=0, columnspan=3, pady=(50, 0), padx=(0, 0), sticky=tk.N)

        self.viewPastEGM = tk.Button(self, text="View Past EGM\nData", width=20, height=6, command=self.view_past_EGM_data_callback)
        self.viewPastEGM.config(font=("Helvetica", 20))
        self.viewPastEGM.grid(row=5, column=0, columnspan=3, pady=(50, 0), padx=(0, 60), sticky=tk.NE)

        self.logoutBtn = tk.Button(self, text="Logout", width=12, height=2, command=self.logout_callback)
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

    def edit_pacing_modes_callback(self):
        self.parent.switch_frame(PacingConfigPage.PacingConfigPage)

    def view_current_EGM_data_callback(self):
        print("Present Data")

    def view_past_EGM_data_callback(self):
        print("Past Data")

    def logout_callback(self):
        self.session_service.invalidate()
        self.parent.switch_frame(LoginPage.LoginPage)