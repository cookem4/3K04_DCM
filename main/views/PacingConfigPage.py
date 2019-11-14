import time
import tkinter as tk
from threading import Thread

from main.data.pacing.PacingMode import PacingMode
from main.data.pacing.modes.AAI import AAI
from main.data.pacing.modes.AAIR import AAIR
from main.data.pacing.modes.AOO import AOO
from main.data.pacing.modes.AOOR import AOOR
from main.data.pacing.modes.DOO import DOO
from main.data.pacing.modes.DOOR import DOOR
from main.data.pacing.modes.VOO import VOO
from main.data.pacing.modes.VOOR import VOOR
from main.data.pacing.modes.VVI import VVI
from main.data.pacing.modes.VVIR import VVIR
from main.views import MainPage
from main.views.AppFrameBase import AppFrameBase

def entry_to_value(entry):
    entry_string = entry.get()
    return float(entry_string) if entry_string != "" else None


class PacingConfigPage(AppFrameBase):
    enabled_bg = "white"
    disabled_bg = "grey"

    def __init__(self, parent):
        super().__init__(parent)

        self.username = self.session_service.get().username

        self.currUserJson = self.load_current_user_json()

        self.usrLowerRateLimit = tk.StringVar()
        self.usrUpperRateLimit = tk.StringVar()
        self.usrAtrialAmp = tk.StringVar()
        self.usrVentricalAmp = tk.StringVar()
        self.usrAtrialPulseWidth = tk.StringVar()
        self.usrVentricalPulseWidth = tk.StringVar()
        self.usrARP = tk.StringVar()
        self.usrVRP = tk.StringVar()
        self.usrActivityThreshold = tk.StringVar()
        self.usrReactionTime = tk.StringVar()
        self.usrRecoveryTime = tk.StringVar()
        self.usrAtrialSensitivity = tk.StringVar()
        self.usrVentricularSensitivity = tk.StringVar()
        self.usrAVDelay = tk.StringVar()

        self.xPadding = 150

        # Vector that tells us what text entry boxes should be shown
        # This one is to display only the boxes for the AOO mode
        self.boxesToDisplay = [True, True, True, False, True, False, False, False, False, False, False, False, False, False]

        self.connectionStateText = tk.Label(self, bg="gray", text="Connection Not Established")
        self.connectionStateText.config(font=("Helvetica", 25), foreground="black")
        # self.connectionStateText.grid(row=0, column=0, columnspan=4, padx=(self.xPadding, 0), pady=(20, 0), sticky=tk.N)
        self.connectionStateText.place(relx=0.325, rely=0.03, anchor='nw')

        self.screenInfo = tk.Label(self, bg="light gray", text="Pacing Mode Configuration", width=50)
        self.screenInfo.config(font=("Helvetica", 30), foreground="black")
        self.screenInfo.grid(row=1, column=0, columnspan=5, padx=(60, 0), pady=(80, 0), sticky=tk.N)

        #################################################
        # The following configues the drop down menu######
        #################################################

        self.pacingModeLabel = tk.Label(self, bg="black", text="Pacing Mode:")
        self.pacingModeLabel.config(font=(25), foreground="white")
        # self.pacingModeLabel.grid(row=2, column=0, padx=(0, 0), pady=(20, 0), sticky=tk.E)
        self.pacingModeLabel.place(relx=0.08, rely=0.25, anchor='nw')

        self.dropDownOptions = ['AOO', 'VOO', 'AAI', 'VVI', 'DOO', 'AOOR', 'VOOR', 'AAIR', 'VVIR', 'DOOR']
        self.pacingSelection = tk.StringVar(self)
        self.pacingSelection.set(self.currUserJson["pacing_mode_name"])
        dropDownMenu = tk.OptionMenu(self, self.pacingSelection, 'AOO', 'VOO', 'AAI', 'VVI', 'DOO', 'AOOR', 'VOOR',
                                     'AAIR', 'VVIR', 'DOOR')
        dropDownMenu.config(font=(25), foreground="white", bg="black")
        # dropDownMenu.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky=tk.W)
        dropDownMenu.place(relx=0.2, rely=0.25, anchor='nw')

        # Sets callback listener for drop down menu
        self.pacingSelection.trace("w", self.drop_down_callback)

        #########################################
        # The following show device information###
        #########################################

        self.programmedModeLabel = tk.Label(self, bg="black", text="Current Programmed Pacing Mode:")
        self.programmedModeLabel.config(font=(20), foreground="white")
        # self.programmedModeLabel.grid(row=3, column=0, columnspan=2, padx=(30, 0), pady=(20, 0), sticky=tk.W)
        self.programmedModeLabel.place(relx=0.05, rely=0.75, anchor='sw')

        self.actualModeLabel = tk.Label(self, bg="black", text=self.currUserJson["pacing_mode_name"])
        self.actualModeLabel.config(font=(20), foreground="white")
        # self.actualModeLabel.grid(row=3, column=1, columnspan=1, padx=(0, 75), pady=(20, 0), sticky=tk.E)
        self.actualModeLabel.place(relx=0.29, rely=0.75, anchor='sw')

        self.currIDLabel = tk.Label(self, bg="black", text="Connected Device ID:")
        self.currIDLabel.config(font=(20), foreground="white")
        # self.currIDLabel.grid(row=4, column=0, columnspan=2, padx=(30, 0), pady=(10, 0), sticky=tk.W)
        self.currIDLabel.place(relx=0.05, rely=0.8, anchor='sw')

        self.currID = tk.Label(self, bg="black", text="None")
        self.currID.config(font=(20), foreground="white")
        # self.currID.grid(row=4, column=0, columnspan=2, padx=(0, 130), pady=(10, 0), sticky=tk.E)
        self.currID.place(relx=0.2, rely=0.8, anchor='sw')

        self.prevIDLabel = tk.Label(self, bg="black", text="Previous Device ID:")
        self.prevIDLabel.config(font=(20), foreground="white")
        # self.prevIDLabel.grid(row=5, column=0, columnspan=2, padx=(30, 0), pady=(10, 0), sticky=tk.W)
        self.prevIDLabel.place(relx=0.05, rely=0.85, anchor='sw')

        self.prevID = tk.Label(self, bg="black", text="None")
        self.prevID.config(font=(20), foreground="white")
        # self.prevID.grid(row=5, column=0, columnspan=2, padx=(0, 140), pady=(10, 0), sticky=tk.E)
        self.prevID.place(relx=0.2, rely=0.85, anchor='sw')

        self.backBtn = tk.Button(self, text="Back", width=10, height=1, command=self.go_back)
        self.backBtn.config(font=("Helvetica", 10))
        # self.backBtn.grid(row=6, column=0, pady=(0, 0), padx=(15, 0), sticky=tk.W)
        self.backBtn.place(relx=0.05, rely=0.92, anchor='sw')

        self.saveBtn = tk.Button(self, text="Save", width=10, height=1, command=self.save_data)
        self.saveBtn.config(font=("Helvetica", 10))
        # self.saveBtn.grid(row=6, column=0, pady=(0, 0), padx=(50, 0), sticky=tk.E)
        self.saveBtn.place(relx=0.12, rely=0.92, anchor='sw')

        self.saveDeviceLabel = tk.Label(self, bg="gray", text="Saving to Device...")
        self.saveDeviceLabel.config(font=(25), foreground="white")
        # self.saveDeviceLabel.grid(row=6, column=1, padx=(30, 0), pady=(0, 0), sticky=tk.W)
        self.saveDeviceLabel.place(relx=0.20, rely=0.92, anchor='sw')

        self.errorLabel = tk.Label(self, bg="black", text="Erroneous Parameters Provided", width=33)

        ###################################################################
        # The following configure the text entries for parameters
        ###################################################################

        self.lowerRateLabel = tk.Label(self, bg="black", text="Lower Rate Limit:")
        self.lowerRateLabel.config(font=(25), foreground="white")

        self.lowerRateLimitEntry = tk.Entry(self, textvariable=self.usrLowerRateLimit, width=10, font=(25),
                                            bg=self.enabled_bg,
                                            disabledbackground=self.disabled_bg)

        self.lowerRateUnitLabel = tk.Label(self, bg="black", text="ppm")
        self.lowerRateUnitLabel.config(font=(25), foreground="white")

        ############################

        self.upperRateLabel = tk.Label(self, bg="black", text="Upper Rate Limit:")
        self.upperRateLabel.config(font=(25), foreground="white")

        self.upperRateLimitEntry = tk.Entry(self, textvariable=self.usrUpperRateLimit, width=10, font=(25),
                                            bg=self.enabled_bg,
                                            disabledbackground=self.disabled_bg)

        self.upperRateUnitLabel = tk.Label(self, bg="black", text="ppm")
        self.upperRateUnitLabel.config(font=(25), foreground="white")

        ############################

        self.atrialAmpLabel = tk.Label(self, bg="black", text="Atrial Amplitude:")
        self.atrialAmpLabel.config(font=(25), foreground="white")

        self.atrialLimitEntry = tk.Entry(self, textvariable=self.usrAtrialAmp, width=10, font=(25), bg=self.enabled_bg,
                                         disabledbackground=self.disabled_bg)

        self.atrialLimitUnit = tk.Label(self, bg="black", text="V")
        self.atrialLimitUnit.config(font=(25), foreground="white")

        #############################

        self.ventricalAmpLabel = tk.Label(self, bg="black", text="Ventricular Amplitude:")
        self.ventricalAmpLabel.config(font=(25), foreground="white")

        self.ventricalLimitEntry = tk.Entry(self, textvariable=self.usrVentricalAmp, width=10, font=(25),
                                            bg=self.enabled_bg,
                                            disabledbackground=self.disabled_bg)

        self.ventricalLimitUnit = tk.Label(self, bg="black", text="V")
        self.ventricalLimitUnit.config(font=(25), foreground="white")

        ############################

        self.atrialPulseWidthLabel = tk.Label(self, bg="black", text="Atrial Pulse Width:")
        self.atrialPulseWidthLabel.config(font=25, foreground="white")

        self.atrialPulseWidthEntry = tk.Entry(self, textvariable=self.usrAtrialPulseWidth, width=10, font=25,
                                              bg=self.enabled_bg,
                                              disabledbackground=self.disabled_bg)

        self.atrialPulseWidthUnit = tk.Label(self, bg="black", text="mSec")
        self.atrialPulseWidthUnit.config(font=(25), foreground="white")

        #########################

        self.ventricalPulseWidthLabel = tk.Label(self, bg="black", text="Ventricular Pulse Width:")
        self.ventricalPulseWidthLabel.config(font=25, foreground="white")

        self.ventricalPulseWidthEntry = tk.Entry(self, textvariable=self.usrVentricalPulseWidth, width=10, font=(25),
                                                 bg=self.enabled_bg,
                                                 disabledbackground=self.disabled_bg)

        self.ventricalPulseWidthUnit = tk.Label(self, bg="black", text="mSec")
        self.ventricalPulseWidthUnit.config(font=(25), foreground="white")

        #########################

        self.arpLabel = tk.Label(self, bg="black", text="ARP:")
        self.arpLabel.config(font=(25), foreground="white")

        self.arpEntry = tk.Entry(self, textvariable=self.usrARP, width=10, font=(25), bg=self.enabled_bg,
                                 disabledbackground=self.disabled_bg)

        self.arpUnit = tk.Label(self, bg="black", text="mSec")
        self.arpUnit.config(font=(25), foreground="white")

        #########################

        self.vrpLabel = tk.Label(self, bg="black", text="VRP:")
        self.vrpLabel.config(font=(25), foreground="white")

        self.vrpEntry = tk.Entry(self, textvariable=self.usrVRP, width=10, font=(25), bg=self.enabled_bg,
                                 disabledbackground=self.disabled_bg)

        self.vrpUnit = tk.Label(self, bg="black", text="mSec")
        self.vrpUnit.config(font=(25), foreground="white")

        #########################

        self.activityThresholdLabel = tk.Label(self, bg="black", text="Activity Threshold:")
        self.activityThresholdLabel.config(font=(25), foreground="white")

        self.activityThresholdEntry = tk.Entry(self, textvariable=self.usrActivityThreshold, width=10, font=(25), bg=self.enabled_bg,
                                        disabledbackground=self.disabled_bg)

        self.activityThresholdUnit = tk.Label(self, bg="black", text="Very Low - High (0-6)")
        self.activityThresholdUnit.config(font=(25), foreground="white")

        #########################

        self.reactionTimeLabel = tk.Label(self, bg="black", text="Reaction Time:")
        self.reactionTimeLabel.config(font=(25), foreground="white")

        self.reactionTimeEntry = tk.Entry(self, textvariable=self.usrReactionTime, width=10, font=(25), bg=self.enabled_bg,
                                        disabledbackground=self.disabled_bg)

        self.reactionTimeUnit = tk.Label(self, bg="black", text="sec")
        self.reactionTimeUnit.config(font=(25), foreground="white")

        #########################

        self.recoveryTimeLabel = tk.Label(self, bg="black", text="Recovery Time:")
        self.recoveryTimeLabel.config(font=(25), foreground="white")

        self.recoveryTimeEntry = tk.Entry(self, textvariable=self.usrRecoveryTime, width=10, font=(25), bg=self.enabled_bg,
                                        disabledbackground=self.disabled_bg)

        self.recoveryTimeUnit = tk.Label(self, bg="black", text="min")
        self.recoveryTimeUnit.config(font=(25), foreground="white")
        
        #########################

        self.avDelayLabel = tk.Label(self, bg="black", text="Fixed AV Delay:")
        self.avDelayLabel.config(font=(25), foreground="white")

        self.avDelayEntry = tk.Entry(self, textvariable=self.usrAVDelay, width=10, font=(25), bg=self.enabled_bg,
                                     disabledbackground=self.disabled_bg)

        self.avDelayUnit = tk.Label(self, bg="black", text="mSec")
        self.avDelayUnit.config(font=(25), foreground="white")

        #########################

        self.atrialSensitivityLabel = tk.Label(self, bg="black", text="Atrial Sensitivity:")
        self.atrialSensitivityLabel.config(font=(25), foreground="white")

        self.atrialSensitivityEntry = tk.Entry(self, textvariable=self.usrAtrialSensitivity, width=10, font=(25),
                                               bg=self.enabled_bg,
                                               disabledbackground=self.disabled_bg)

        self.atrialSensitivityUnit = tk.Label(self, bg="black", text="mV")
        self.atrialSensitivityUnit.config(font=(25), foreground="white")

        #########################

        self.ventricularSensitivityLabel = tk.Label(self, bg="black", text="Ventricular Sensitivity:")
        self.ventricularSensitivityLabel.config(font=(25), foreground="white")

        self.ventricularSensitivityEntry = tk.Entry(self, textvariable=self.usrVentricularSensitivity, width=10,
                                                    font=(25), bg=self.enabled_bg,
                                                    disabledbackground=self.disabled_bg)

        self.ventricularSensitivityUnit = tk.Label(self, bg="black", text="mV")
        self.ventricularSensitivityUnit.config(font=(25), foreground="white")

        #################################

        self.drop_down_callback()

        #################################

        # Set textbox values based on user profile
        # String slicing of json object

        # print(self.currUserJson["pacing_mode_settings"])
        lowerRateLimitSlice = self.currUserJson["pacing_mode_settings"][
                              self.currUserJson["pacing_mode_settings"].index("lower_rate_limit\": ") + len(
                                  "lower_rate_limit\": "):self.currUserJson["pacing_mode_settings"].index(
                                  ", \"upper_rate_limit\": ")]
        upperRateLimitSlice = self.currUserJson["pacing_mode_settings"][
                              self.currUserJson["pacing_mode_settings"].index("upper_rate_limit\": ") + len(
                                  "upper_rate_limit\": "):self.currUserJson["pacing_mode_settings"].index(
                                  ", \"atrial_amplitude\": ")]
        atrialAmpSlice = self.currUserJson["pacing_mode_settings"][
                         self.currUserJson["pacing_mode_settings"].index("atrial_amplitude\": ") + len(
                             "atrial_amplitude\": "):self.currUserJson["pacing_mode_settings"].index(
                             ", \"atrial_pulse_width\": ")]
        atrialPulseWidthSlice = self.currUserJson["pacing_mode_settings"][
                                self.currUserJson["pacing_mode_settings"].index("atrial_pulse_width\": ") + len(
                                    "atrial_pulse_width\": "):self.currUserJson["pacing_mode_settings"].index(
                                    ", \"ventricular_amplitude\": ")]
        ventricalAmpSlice = self.currUserJson["pacing_mode_settings"][
                            self.currUserJson["pacing_mode_settings"].index("ventricular_amplitude\": ") + len(
                                "ventricular_amplitude\": "):self.currUserJson["pacing_mode_settings"].index(
                                ", \"ventricular_pulse_width\": ")]
        ventricalPulseWidthSlice = self.currUserJson["pacing_mode_settings"][
                                   self.currUserJson["pacing_mode_settings"].index("ventricular_pulse_width\": ") + len(
                                       "ventricular_pulse_width\": "):self.currUserJson["pacing_mode_settings"].index(
                                       ", \"arp\": ")]
        arpSlice = self.currUserJson["pacing_mode_settings"][
                   self.currUserJson["pacing_mode_settings"].index("arp\": ") + len("arp\": "):self.currUserJson[
                       "pacing_mode_settings"].index(", \"vrp\": ")]
        vrpSlice = self.currUserJson["pacing_mode_settings"][
                   self.currUserJson["pacing_mode_settings"].index("vrp\": ") + len("vrp\": "):self.currUserJson[
                       "pacing_mode_settings"].index(", \"activity_threshold\": ")]
        activityThresholdSlice = self.currUserJson["pacing_mode_settings"][
                          self.currUserJson["pacing_mode_settings"].index("activity_threshold\": ") + len("activity_threshold\": "):
                          self.currUserJson[
                              "pacing_mode_settings"].index(", \"reaction_time\": ")]
        reactionTimeSlice = self.currUserJson["pacing_mode_settings"][
                          self.currUserJson["pacing_mode_settings"].index("reaction_time\": ") + len("reaction_time\": "):
                          self.currUserJson[
                              "pacing_mode_settings"].index(", \"recovery_time\": ")]
        recoveryTimeSlice = self.currUserJson["pacing_mode_settings"][
                          self.currUserJson["pacing_mode_settings"].index("recovery_time\": ") + len("recovery_time\": "):
                          self.currUserJson[
                              "pacing_mode_settings"].index(", \"av_delay\": ")]
        avDelaySlice = self.currUserJson["pacing_mode_settings"][
                       self.currUserJson["pacing_mode_settings"].index("av_delay\": ") + len("av_delay\": "):
                       self.currUserJson[
                           "pacing_mode_settings"].index(", \"atrial_sensitivity\": ")]
        atrialSensitivitySlice = self.currUserJson["pacing_mode_settings"][
                                 self.currUserJson["pacing_mode_settings"].index("atrial_sensitivity\": ") + len(
                                     "atrial_sensitivity\": "):self.currUserJson[
                                     "pacing_mode_settings"].index(", \"ventricular_sensitivity\": ")]
        ventricularSensitivitySlice = self.currUserJson["pacing_mode_settings"][
                                      self.currUserJson["pacing_mode_settings"].index(
                                          "ventricular_sensitivity\": ") + len("ventricular_sensitivity\": "):
                                      self.currUserJson[
                                          "pacing_mode_settings"].index("}")]

        self.usrLowerRateLimit.set("" if (lowerRateLimitSlice == "null") else (lowerRateLimitSlice))
        self.usrUpperRateLimit.set("" if (upperRateLimitSlice == "null") else upperRateLimitSlice)
        self.usrAtrialAmp.set("" if (atrialAmpSlice == "null") else atrialAmpSlice)
        self.usrAtrialPulseWidth.set("" if (atrialPulseWidthSlice == "null") else atrialPulseWidthSlice)
        self.usrVentricalAmp.set("" if (ventricalAmpSlice == "null") else ventricalAmpSlice)
        self.usrVentricalPulseWidth.set("" if (ventricalPulseWidthSlice == "null") else ventricalPulseWidthSlice)
        self.usrARP.set("" if (arpSlice == "null") else arpSlice)
        self.usrVRP.set("" if (vrpSlice == "null") else vrpSlice)
        self.usrActivityThreshold.set("" if (activityThresholdSlice == "null") else activityThresholdSlice)
        self.usrReactionTime.set("" if (reactionTimeSlice == "null") else reactionTimeSlice)
        self.usrRecoveryTime.set("" if (recoveryTimeSlice == "null") else recoveryTimeSlice)
        self.usrAVDelay.set("" if (avDelaySlice == "null") else avDelaySlice)
        self.usrAtrialSensitivity.set("" if (atrialSensitivitySlice == "null") else atrialSensitivitySlice)
        self.usrVentricularSensitivity.set(
            "" if (ventricularSensitivitySlice == "null") else ventricularSensitivitySlice)

        #Set up labels based on pacing status
        if self.serial_indicators.isConnected():
            self.connectionStateText.config(text="Connection Established", foreground="white",
                                            background="green")
            if self.serial_indicators.getLastConnectionID() is not None or self.serial_indicators.getCurrConnectionID() is not None:
                self.currID.config(text=str(self.serial_indicators.getCurrConnectionID()))
                self.prevID.config(text=str(self.serial_indicators.getLastConnectionID()))
            else:
                self.currID.config(text="None")
                self.prevID.config(text="None")
        else:
            self.connectionStateText.config(text="Connection Not Established", foreground="black",
                                            background="gray")
            self.currID.config(text="None")
            self.prevID.config(text="None")

        # Set up background thread
        self.threadController = True
        self.isConnectionEstablished = False
        self.myThread = Thread(target=self.MyThread, args=())
        self.myThread.start()

    def load_current_user_json(self):
        return self.user_service.read(self.username).to_json()

    def drop_down_callback(self, *args):
        # Upon callback clear all boxes
        self.lowerRateLimitEntry.delete(0, tk.END)
        self.upperRateLimitEntry.delete(0, tk.END)
        self.atrialLimitEntry.delete(0, tk.END)
        self.ventricalLimitEntry.delete(0, tk.END)
        self.atrialPulseWidthEntry.delete(0, tk.END)
        self.ventricalPulseWidthEntry.delete(0, tk.END)
        self.arpEntry.delete(0, tk.END)
        self.vrpEntry.delete(0, tk.END)
        self.activityThresholdEntry.delete(0, tk.END)
        self.reactionTimeEntry.delete(0, tk.END)
        self.recoveryTimeEntry.delete(0, tk.END)
        self.avDelayEntry.delete(0, tk.END)
        self.atrialSensitivityEntry.delete(0, tk.END)
        self.ventricularSensitivityEntry.delete(0, tk.END)

        # Sets which boxes are grayed out based on drop down menu selection
        # Update variables based on drop down selection
        if self.pacingSelection.get() == "AOO":
            self.boxesToDisplay = [True, True, True, False, True, False, False, False, False, False, False, False, False, False]
            # self.set_states(VLE="disabled", VPW="disabled", ARP="disabled", VRP="disabled")
        if self.pacingSelection.get() == "VOO":
            self.boxesToDisplay = [True, True, False, True, False, True, False, False, False, False, False, False, False, False]
            # self.set_states(ALE="disabled", APW="disabled", ARP="disabled", VRP="disabled")
        if self.pacingSelection.get() == "AAI":
            self.boxesToDisplay = [True, True, True, False, True, False, True, False, False, False, False, False, False, False]
            # self.set_states(VLE="disabled", VPW="disabled", VRP="disabled")
        if self.pacingSelection.get() == "VVI":
            self.boxesToDisplay = [True, True, False, True, False, True, False, True, False, False, False, False, False, False]
            # self.set_states(ALE="disabled", APW="disabled", ARP="disabled")
        if self.pacingSelection.get() == "DOO":
            self.boxesToDisplay = [True, True, True, True, True, True, False, False, False, False, False, True, False, False]
        if self.pacingSelection.get() == "AOOR":
            self.boxesToDisplay = [True, True, True, False, True, False, False, False, True, True, True, False, False, False]
        if self.pacingSelection.get() == "VOOR":
            self.boxesToDisplay = [True, True, False, True, False, True, False, False, True, True, True, False, False, False]
        if self.pacingSelection.get() == "AAIR":
            self.boxesToDisplay = [True, True, True, False, True, False, True, False, True, True, True, False, True, False]
        if self.pacingSelection.get() == "VVIR":
            self.boxesToDisplay = [True, True, False, True, False, True, False, True, True, True, True, False, False, True]
        if self.pacingSelection.get() == "DOOR":
            self.boxesToDisplay = [True, True, True, True, True, True, False, False, True, True, True, True, False, False]
        # Show only if the corresponding vector element is true
        rowCounter = 0.25  # keeps track of what row the entry box is to be displayed in
        if (self.boxesToDisplay[0]):
            '''
            self.lowerRateLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(50, 0), sticky=tk.E)
            self.lowerRateLimitEntry.grid(row=rowCounter, column=3, pady=(50, 0), padx=(15, 0), sticky=tk.W)
            self.lowerRateUnitLabel.grid(row=rowCounter, column=3, padx=(0, 20), pady=(50, 0), sticky=tk.E)
            '''
            self.lowerRateLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.lowerRateLimitEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.lowerRateUnitLabel.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.lowerRateLabel.place_forget()
            self.lowerRateLimitEntry.place_forget()
            self.lowerRateUnitLabel.place_forget()
        if (self.boxesToDisplay[1]):
            '''
            self.upperRateLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)
            self.upperRateLimitEntry.grid(row=rowCounter, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)
            self.upperRateUnitLabel.grid(row=rowCounter, column=3, padx=(0, 20), pady=(20, 0), sticky=tk.E)
            rowCounter = rowCounter + 1
            '''
            self.upperRateLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.upperRateLimitEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.upperRateUnitLabel.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.upperRateLabel.place_forget()
            self.upperRateLimitEntry.place_forget()
            self.upperRateUnitLabel.place_forget()
        if (self.boxesToDisplay[2]):
            ''''
            self.atrialAmpLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)
            self.atrialLimitEntry.grid(row=rowCounter, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)
            self.atrialLimitUnit.grid(row=rowCounter, column=3, padx=(0, 35), pady=(20, 0), sticky=tk.E)
            rowCounter = rowCounter + 1
            '''
            self.atrialAmpLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.atrialLimitEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.atrialLimitUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.atrialAmpLabel.place_forget()
            self.atrialLimitEntry.place_forget()
            self.atrialLimitUnit.place_forget()
        if (self.boxesToDisplay[3]):
            '''
            self.ventricalAmpLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)
            self.ventricalLimitEntry.grid(row=rowCounter, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)
            self.ventricalLimitUnit.grid(row=rowCounter, column=3, padx=(0, 35), pady=(20, 0), sticky=tk.E)
            rowCounter = rowCounter + 1
            '''
            self.ventricalAmpLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.ventricalLimitEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.ventricalLimitUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.ventricalAmpLabel.place_forget()
            self.ventricalLimitEntry.place_forget()
            self.ventricalLimitUnit.place_forget()
        if (self.boxesToDisplay[4]):
            '''
            self.atrialPulseWidthLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)
            self.atrialPulseWidthEntry.grid(row=rowCounter, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)
            self.atrialPulseWidthUnit.grid(row=rowCounter, column=3, padx=(0, 15), pady=(20, 0), sticky=tk.E)
            rowCounter = rowCounter + 1
            '''
            self.atrialPulseWidthLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.atrialPulseWidthEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.atrialPulseWidthUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.atrialPulseWidthLabel.place_forget()
            self.atrialPulseWidthEntry.place_forget()
            self.atrialPulseWidthUnit.place_forget()
        if (self.boxesToDisplay[5]):
            '''
            self.ventricalPulseWidthLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)
            self.ventricalPulseWidthEntry.grid(row=rowCounter, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)
            self.ventricalPulseWidthUnit.grid(row=rowCounter, column=3, padx=(0, 15), pady=(20, 0), sticky=tk.E)
            rowCounter = rowCounter + 1
            '''
            self.ventricalPulseWidthLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.ventricalPulseWidthEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.ventricalPulseWidthUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.ventricalPulseWidthLabel.place_forget()
            self.ventricalPulseWidthEntry.place_forget()
            self.ventricalPulseWidthUnit.place_forget()
        if (self.boxesToDisplay[6]):
            '''
            self.arpLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)
            self.arpEntry.grid(row=rowCounter, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)
            self.arpUnit.grid(row=rowCounter, column=3, padx=(0, 10), pady=(20, 0), sticky=tk.E)
            rowCounter = rowCounter + 1
            '''
            self.arpLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.arpEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.arpUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.arpLabel.place_forget()
            self.arpEntry.place_forget()
            self.arpUnit.place_forget()
        if (self.boxesToDisplay[7]):
            '''
            self.vrpLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)
            self.vrpEntry.grid(row=rowCounter, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)
            self.vrpUnit.grid(row=rowCounter, column=3, padx=(0, 10), pady=(20, 0), sticky=tk.E)
            rowCounter = rowCounter + 1
            '''
            self.vrpLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.vrpEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.vrpUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.vrpLabel.place_forget()
            self.vrpEntry.place_forget()
            self.vrpUnit.place_forget()
        if (self.boxesToDisplay[8]):
            self.activityThresholdLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.activityThresholdEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.activityThresholdUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.activityThresholdLabel.place_forget()
            self.activityThresholdEntry.place_forget()
            self.activityThresholdUnit.place_forget()
        if (self.boxesToDisplay[9]):
            self.reactionTimeLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.reactionTimeEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.reactionTimeUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.reactionTimeLabel.place_forget()
            self.reactionTimeEntry.place_forget()
            self.reactionTimeUnit.place_forget()
        if (self.boxesToDisplay[10]):
            self.recoveryTimeLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.recoveryTimeEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.recoveryTimeUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.recoveryTimeLabel.place_forget()
            self.recoveryTimeEntry.place_forget()
            self.recoveryTimeUnit.place_forget()
        if (self.boxesToDisplay[11]):
            '''
            self.avDelayLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)
            self.avDelayEntry.grid(row=rowCounter, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)
            self.avDelayUnit.grid(row=rowCounter, column=3, padx=(0, 10), pady=(20, 0), sticky=tk.E)
            rowCounter = rowCounter + 1
            '''
            self.avDelayLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.avDelayEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.avDelayUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.avDelayLabel.place_forget()
            self.avDelayEntry.place_forget()
            self.avDelayUnit.place_forget()
        if (self.boxesToDisplay[12]):
            '''
            self.atrialSensitivityLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)
            self.atrialSensitivityEntry.grid(row=rowCounter, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)
            self.atrialSensitivityUnit.grid(row=rowCounter, column=3, padx=(0, 10), pady=(20, 0), sticky=tk.E)
            rowCounter = rowCounter + 1
            '''
            self.atrialSensitivityLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.atrialSensitivityEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.atrialSensitivityUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.atrialSensitivityLabel.place_forget()
            self.atrialSensitivityEntry.place_forget()
            self.atrialSensitivityUnit.place_forget()
        if (self.boxesToDisplay[13]):
            '''
            self.ventricularSensitivityLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)
            self.ventricularSensitivityEntry.grid(row=rowCounter, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)
            self.ventricularSensitivityUnit.grid(row=rowCounter, column=3, padx=(0, 10), pady=(20, 0), sticky=tk.E)
            rowCounter = rowCounter + 1
            '''
            self.ventricularSensitivityLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.ventricularSensitivityEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.ventricularSensitivityUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.ventricularSensitivityLabel.place_forget()
            self.ventricularSensitivityEntry.place_forget()
            self.ventricularSensitivityUnit.place_forget()

    def set_states(self, LRL="normal", URL="normal", ALE="normal", VLE="normal", APW="normal", VPW="normal",
                   ARP="normal", VRP="normal"):
        self.lowerRateLimitEntry.config(state=LRL)
        self.upperRateLimitEntry.config(state=URL)
        self.atrialLimitEntry.config(state=ALE)
        self.ventricalLimitEntry.config(state=VLE)
        self.atrialPulseWidthEntry.config(state=APW)
        self.ventricalPulseWidthEntry.config(state=VPW)
        self.arpEntry.config(state=ARP)
        self.vrpEntry.config(state=VRP)

    def go_back(self):
        self.parent.switch_frame(MainPage.MainPage)
        self.threadController = False

    def save_data(self):
        # Update variables based on drop down selection
        pacingErrorStr = "Entries cannot be empty"
        try:
            pacing_mode: PacingMode = PacingMode(
                lower_rate_limit=entry_to_value(self.lowerRateLimitEntry),
                upper_rate_limit=entry_to_value(self.upperRateLimitEntry),
                atrial_amplitude=entry_to_value(self.atrialLimitEntry),
                atrial_pulse_width=entry_to_value(self.atrialPulseWidthEntry),
                ventricular_amplitude=entry_to_value(self.ventricalLimitEntry),
                ventricular_pulse_width=entry_to_value(self.ventricalPulseWidthEntry),
                arp=entry_to_value(self.arpEntry),
                vrp=entry_to_value(self.vrpEntry),
                activity_threshold=entry_to_value(self.activityThresholdEntry),
                reaction_time=entry_to_value(self.reactionTimeEntry),
                recovery_time=entry_to_value(self.recoveryTimeEntry),
                av_delay=entry_to_value(self.avDelayEntry),
                atrial_sensitivity=entry_to_value(self.atrialSensitivityEntry),
                ventricular_sensitivity=entry_to_value(self.ventricularSensitivityEntry))
            
            if self.pacingSelection.get() == "AOO":
                pacing_mode.__class__ = AOO
            if self.pacingSelection.get() == "VOO":
                pacing_mode.__class__ = VOO
            if self.pacingSelection.get() == "AAI":
                pacing_mode.__class__ = AAI
            if self.pacingSelection.get() == "VVI":
                pacing_mode.__class__ = VVI
            if self.pacingSelection.get() == "DOO":
                pacing_mode.__class__ = DOO
            if self.pacingSelection.get() == "AOOR":
                pacing_mode.__class__ = AOOR
            if self.pacingSelection.get() == "DOOR":
                pacing_mode.__class__ = DOOR
            if self.pacingSelection.get() == "VVIR":
                pacing_mode.__class__ = VVIR
            if self.pacingSelection.get() == "AAIR":
                pacing_mode.__class__ = AAIR
            if self.pacingSelection.get() == "VOOR":
                pacing_mode.__class__ = VOOR

            pacingErrorStr = pacing_mode.validation_result.error
            display_error_message = not pacing_mode.validation_result.success
        except Exception as e:
            print(e)
            display_error_message = True  # If non numerical entries

        if display_error_message:
            self.errorLabel.config(font=(25), foreground="red")
            self.errorLabel.config(text=pacingErrorStr, width=50)
            # self.errorLabel.grid(row=10, column=2, columnspan=3, padx=(0, 0), pady=(0, 0), sticky=tk.E)
            self.errorLabel.place(relx=0.05, rely=0.5, anchor='sw')
        else:
            # Update saved pacing mode based on username and drop down selection
            self.user_service.update_pacing_mode(self.username, pacing_mode)

            self.errorLabel.config(text="", width=1)  # Shrink to remove, deleting wasn't working


            # Update displayed programmed mode
            self.currUserJson = self.load_current_user_json()
            self.actualModeLabel.config(text=self.currUserJson["pacing_mode_name"])

            '''
            # Update saving indicator
            self.saveDeviceLabel.config(bg="green", fg="black")
            tk.Tk().after(200, lambda: self.saveDeviceLabel.config(bg="gray", fg="white"))
            tk.Tk().after(200, lambda: self.saveDeviceLabel.config(bg="green", fg="black"))
            tk.Tk().after(200, lambda: self.saveDeviceLabel.config(bg="gray", fg="white"))
            tk.Tk().after(200, lambda: self.saveDeviceLabel.config(bg="green", fg="black"))
            tk.Tk().after(200, lambda: self.saveDeviceLabel.config(bg="gray", fg="white"))
            tk.Tk().after(200, lambda: self.saveDeviceLabel.config(bg="green", fg="black"))
            tk.Tk().after(200, lambda: self.saveDeviceLabel.config(bg="gray", fg="white"))
            tk.Tk().after(200, lambda: self.saveDeviceLabel.config(bg="green", fg="black"))
            tk.Tk().after(200, lambda: self.saveDeviceLabel.config(bg="gray", fg="white"))
            '''
            # transmit serial data:
            self.serial_service.send_pacing_data(pacing_mode)


    # Thread to check connection status. Condition will change to self.serial_service.is_connection_established()
    # This is essentially a background thread for serial data
    def MyThread(self):
        # start by trying to connect to the pacemaker
        if not self.serial_indicators.isConnected():
            self.serial_service.connect_to_pacemaker()
            if self.serial_service.is_connection_established():
                self.serial_indicators.setConnection(True)
                self.serial_indicators.setCurrConnectionID(self.serial_service.get_device_ID())
                self.serial_indicators.setLastConnectionID(self.serial_service.get_last_device_connected())

        while self.threadController:
            if not self.threadController:
                break
            time.sleep(1)
            if not self.threadController:
                break
            if self.serial_indicators.isConnected():
                self.connectionStateText.config(text="Connection Established", foreground="white",
                                                background="green")
                if self.serial_indicators.getLastConnectionID() is not None or self.serial_indicators.getCurrConnectionID() is not None:
                    self.currID.config(text=str(self.serial_indicators.getCurrConnectionID()))
                    self.prevID.config(text=str(self.serial_indicators.getLastConnectionID()))
                else:
                    self.currID.config(text="None")
                    self.prevID.config(text="None")
            else:
                self.connectionStateText.config(text="Connection Not Established", foreground="black",
                                                background="gray")
                self.currID.config(text="None")
                self.prevID.config(text="None")
                print("NOT CONNECTED")
