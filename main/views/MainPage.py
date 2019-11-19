import tkinter as tk

from main.views import PacingConfigPage, LoginPage, EGMDataPage
from main.views.AppFrameBase import AppFrameBase
import time
from threading import Thread


class MainPage(AppFrameBase):
    def __init__(self, parent):
        super().__init__(parent)

        username = self.session_service.get().username
        self.currUserJson = self.user_service.read(username).to_json()

        self.connectionStateText = tk.Label(self, bg="gray", text="Connection Not Established")
        self.connectionStateText.config(font=("Helvetica", 25), foreground="black")
        self.connectionStateText.grid(row=0, column=0, columnspan=4, padx=(0, 0), pady=(20, 0), sticky=tk.N)

        self.screenInfo = tk.Label(self, bg="light gray", text="HOME", width=48)
        self.screenInfo.config(font=("Helvetica", 35), foreground="black")
        self.screenInfo.grid(row=1, column=0, columnspan=3, padx=(0, 0), pady=(20, 0), sticky=tk.N)

        self.editPacingButton = tk.Button(self, text="Edit Pacing Mode\nand Parameters", width=25, height=6,
                                          command=self.edit_pacing_modes_callback)
        self.editPacingButton.config(font=("Helvetica", 20))
        self.editPacingButton.grid(row=5, column=0, columnspan=3, pady=(50, 0), padx=(175, 0), sticky=tk.NW)

        self.viewCurrEGM = tk.Button(self, text="View EGM\nData", width=25, height=6,
                                     command=self.view_current_EGM_data_callback)
        self.viewCurrEGM.config(font=("Helvetica", 20))
        self.viewCurrEGM.grid(row=5, column=0, columnspan=3, pady=(50, 0), padx=(0, 175), sticky=tk.NE)

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

        self.currIDLabel = tk.Label(self, bg="black", text="Connected Device ID: None")
        self.currIDLabel.config(font=(15), foreground="white")
        self.currIDLabel.grid(row=3, column=0, columnspan=3, padx=(0, 0), pady=(0, 0), sticky=tk.N)

        self.prevIDLabel = tk.Label(self, bg="black", text="Previous Device ID: None")
        self.prevIDLabel.config(font=(15), foreground="white")
        self.prevIDLabel.grid(row=4, column=0, columnspan=3, padx=(0, 0), pady=(0, 0), sticky=tk.N)

        if self.serial_indicators.isConnected():
            self.connectionStateText.config(text="Connection Established", foreground="white", background="green")
            if self.serial_indicators.getCurrConnectionID() is not None or self.serial_indicators.getLastConnectionID() is not None:
                self.currIDLabel.config(
                    text="Connected Device ID: " + str(self.serial_indicators.getCurrConnectionID()))
                self.prevIDLabel.config(text="Previous Device ID: " + str(self.serial_indicators.getLastConnectionID()))
            else:
                self.currIDLabel.config(text="Connected Device ID: None")
                self.prevIDLabel.config(text="Previous Device ID: None")
        else:
            self.connectionStateText.config(text="Connection Not Established", foreground="black", background="gray")
            self.currIDLabel.config(text="Connected Device ID: None")
            self.prevIDLabel.config(text="Previous Device ID: None")

        self.threadController = True
        self.myThread = Thread(target = self.ConnectionThread, args = ())
        self.myThread.start()

    def edit_pacing_modes_callback(self):
        self.threadController = False
        self.parent.switch_frame(PacingConfigPage.PacingConfigPage)


    def view_current_EGM_data_callback(self):
        self.parent.switch_frame(EGMDataPage.EGMDataPage)
        self.threadController = False

    def logout_callback(self):
        self.session_service.invalidate()
        self.parent.switch_frame(LoginPage.LoginPage)
        self.threadController = False
        self.serial_service.disconnect_from_pacemaker()
        self.serial_indicators.setConnection(False)
        self.serial_indicators.setLastConnectionID(None)
        self.serial_indicators.setCurrConnectionID(None)



    #Thread to check connection status. Condition will change to self.serial_service.is_connection_established()
    #This is essentially a background thread for serial data
    def ConnectionThread(self):
        # start by trying to connect to the pacemaker
        if not self.serial_indicators.isConnected():
            self.serial_service.connect_to_pacemaker()
        if self.serial_service.is_connection_established():
            self.serial_indicators.setConnection(True)
            self.serial_indicators.setCurrConnectionID(self.serial_service.get_device_ID())
            self.serial_indicators.setLastConnectionID(self.serial_service.get_last_device_connected())
        if self.serial_indicators.isConnected():
            self.connectionStateText.config(text="Connection Established", foreground="white",
                                            background="green")
            if self.serial_indicators.getCurrConnectionID() is not None or self.serial_indicators.getLastConnectionID() is not None:
                self.currIDLabel.config(
                    text="Connected Device ID: " + str(self.serial_indicators.getCurrConnectionID()))
                self.prevIDLabel.config(
                    text="Previous Device ID: " + str(self.serial_indicators.getLastConnectionID()))
            else:
                self.currIDLabel.config(text="Connected Device ID: None")
                self.prevIDLabel.config(text="Previous Device ID: None")
            print("CONNECTED")
        else:
            self.connectionStateText.config(text="Connection Not Established", foreground="black",
                                            background="gray")
            self.currIDLabel.config(text="Connected Device ID: None")
            self.prevIDLabel.config(text="Previous Device ID: None")
            print("NOT CONNECTED")
        i=0
        lastDisconnectCheck = int(round(time.time() * 1000))
        while self.threadController:
            time.sleep(0.5)
            print("HERE" + str(i))
            i = i + 1
            if int(round(time.time() * 1000)) - lastDisconnectCheck > 5000:
                if self.serial_service.is_connection_established():
                    self.serial_indicators.setConnection(True)
                    self.serial_indicators.setCurrConnectionID(self.serial_service.get_device_ID())
                    self.serial_indicators.setLastConnectionID(self.serial_service.get_last_device_connected())
                else:
                    self.serial_indicators.setConnection(False)
                    self.serial_indicators.setCurrConnectionID(None)
                    self.serial_indicators.setLastConnectionID(None)
                lastDisconnectCheck = int(round(time.time() * 1000))
                if self.serial_indicators.isConnected():
                    self.connectionStateText.config(text="Connection Established", foreground="white",
                                                    background="green")
                    if self.serial_indicators.getCurrConnectionID() is not None or self.serial_indicators.getLastConnectionID() is not None:
                        self.currIDLabel.config(
                            text="Connected Device ID: " + str(self.serial_indicators.getCurrConnectionID()))
                        self.prevIDLabel.config(
                            text="Previous Device ID: " + str(self.serial_indicators.getLastConnectionID()))
                    else:
                        self.currIDLabel.config(text="Connected Device ID: None")
                        self.prevIDLabel.config(text="Previous Device ID: None")
                    print("CONNECTED")
                else:
                    self.connectionStateText.config(text="Connection Not Established", foreground="black",
                                                    background="gray")
                    self.currIDLabel.config(text="Connected Device ID: None")
                    self.prevIDLabel.config(text="Previous Device ID: None")
                    print("NOT CONNECTED")
