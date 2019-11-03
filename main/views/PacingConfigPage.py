import tkinter as tk

from main.data.PacingMode import PacingMode
from main.data.pacingmodes.AAI import AAI
from main.data.pacingmodes.AAIR import AAIR
from main.data.pacingmodes.AOO import AOO
from main.data.pacingmodes.AOOR import AOOR
from main.data.pacingmodes.DOO import DOO
from main.data.pacingmodes.DOOR import DOOR
from main.data.pacingmodes.VOO import VOO
from main.data.pacingmodes.VOOR import VOOR
from main.data.pacingmodes.VVI import VVI
from main.data.pacingmodes.VVIR import VVIR
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
        self.usrSensorRate = tk.StringVar()
        self.usrAtrialSensitivity = tk.StringVar()
        self.usrVentricularSensitivity = tk.StringVar()
        self.usrAVDelay = tk.StringVar()

        self.xPadding = 150

        # Vector that tells us what text entry boxes should be shown
        # This one is to display only the boxes for the AOO mode
        self.boxesToDisplay = [True, True, True, False, True, False, False, False, False, False, False, False]

        self.connectionStateText = tk.Label(self, bg="gray", text="Connection Not Established")
        self.connectionStateText.config(font=("Helvetica", 25), foreground="white")
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

        self.currID = tk.Label(self, bg="black", text="123456")
        self.currID.config(font=(20), foreground="white")
        # self.currID.grid(row=4, column=0, columnspan=2, padx=(0, 130), pady=(10, 0), sticky=tk.E)
        self.currID.place(relx=0.2, rely=0.8, anchor='sw')

        self.prevIDLabel = tk.Label(self, bg="black", text="Previous Device ID:")
        self.prevIDLabel.config(font=(20), foreground="white")
        # self.prevIDLabel.grid(row=5, column=0, columnspan=2, padx=(30, 0), pady=(10, 0), sticky=tk.W)
        self.prevIDLabel.place(relx=0.05, rely=0.85, anchor='sw')

        self.prevID = tk.Label(self, bg="black", text="654321")
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

        self.sensorRateLabel = tk.Label(self, bg="black", text="Max Sensor Rate:")
        self.sensorRateLabel.config(font=(25), foreground="white")

        self.sensorRateEntry = tk.Entry(self, textvariable=self.usrSensorRate, width=10, font=(25), bg=self.enabled_bg,
                                        disabledbackground=self.disabled_bg)

        self.sensorRateUnit = tk.Label(self, bg="black", text="mSec")
        self.sensorRateUnit.config(font=(25), foreground="white")

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
        '''
        print(self.currUserJson["pacing_mode_settings"])
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
                       "pacing_mode_settings"].index(", \"sensor_rate\": ")]
        sensorRateSlice = self.currUserJson["pacing_mode_settings"][
                          self.currUserJson["pacing_mode_settings"].index("sensor_rate\": ") + len("sensor_rate\": "):
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
        self.usrSensorRate.set("" if (sensorRateSlice == "null") else sensorRateSlice)
        self.usrAVDelay.set("" if (avDelaySlice == "null") else avDelaySlice)
        self.usrAtrialSensitivity.set("" if (atrialSensitivitySlice == "null") else atrialSensitivitySlice)
        self.usrVentricularSensitivity.set(
            "" if (ventricularSensitivitySlice == "null") else ventricularSensitivitySlice)
        '''
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
        self.sensorRateEntry.delete(0, tk.END)
        self.avDelayEntry.delete(0, tk.END)
        self.atrialSensitivityEntry.delete(0, tk.END)
        self.ventricularSensitivityEntry.delete(0, tk.END)

        # Sets which boxes are grayed out based on drop down menu selection
        # Update variables based on drop down selection
        if self.pacingSelection.get() == "AOO":
            self.boxesToDisplay = [True, True, True, False, True, False, False, False, False, False, False, False]
            # self.set_states(VLE="disabled", VPW="disabled", ARP="disabled", VRP="disabled")
        if self.pacingSelection.get() == "VOO":
            self.boxesToDisplay = [True, True, False, True, False, True, False, False, False, False, False, False]
            # self.set_states(ALE="disabled", APW="disabled", ARP="disabled", VRP="disabled")
        if self.pacingSelection.get() == "AAI":
            self.boxesToDisplay = [True, True, True, False, True, False, True, False, False, False, False, False]
            # self.set_states(VLE="disabled", VPW="disabled", VRP="disabled")
        if self.pacingSelection.get() == "VVI":
            self.boxesToDisplay = [True, True, False, True, False, True, False, True, False, False, False, False]
            # self.set_states(ALE="disabled", APW="disabled", ARP="disabled")
        if self.pacingSelection.get() == "DOO":
            self.boxesToDisplay = [True, True, True, True, True, True, False, False, False, True, False, False]
        if self.pacingSelection.get() == "AOOR":
            self.boxesToDisplay = [True, True, True, False, True, False, False, False, True, False, False, False]
        if self.pacingSelection.get() == "VOOR":
            self.boxesToDisplay = [True, True, False, True, False, True, False, False, True, False, False, False]
        if self.pacingSelection.get() == "AAIR":
            self.boxesToDisplay = [True, True, True, False, True, False, True, False, True, False, True, False]
        if self.pacingSelection.get() == "VVIR":
            self.boxesToDisplay = [True, True, False, True, False, True, False, True, True, False, False, True]
        if self.pacingSelection.get() == "DOOR":
            self.boxesToDisplay = [True, True, True, True, True, True, False, False, True, True, False, False]
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
            '''
            self.sensorRateLabel.grid(row=rowCounter, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)
            self.sensorRateEntry.grid(row=rowCounter, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)
            self.sensorRateUnit.grid(row=rowCounter, column=3, padx=(0, 10), pady=(20, 0), sticky=tk.E)
            rowCounter = rowCounter + 1
            '''
            self.sensorRateLabel.place(relx=0.53, rely=rowCounter, anchor='sw')
            self.sensorRateEntry.place(relx=0.7, rely=rowCounter, anchor='sw')
            self.sensorRateUnit.place(relx=0.78, rely=rowCounter, anchor='sw')
            rowCounter = rowCounter + 0.08
        else:
            self.sensorRateLabel.place_forget()
            self.sensorRateEntry.place_forget()
            self.sensorRateUnit.place_forget()
        if (self.boxesToDisplay[9]):
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
        if (self.boxesToDisplay[10]):
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
        if (self.boxesToDisplay[11]):
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

    def save_data(self):
        # Update variables based on drop down selection
        try:
            pacing_mode: PacingMode = PacingMode(lower_rate_limit=entry_to_value(self.lowerRateLimitEntry),
										 upper_rate_limit=entry_to_value(self.upperRateLimitEntry),
										 atrial_amplitude=entry_to_value(self.atrialLimitEntry),
										 atrial_pulse_width=entry_to_value(self.atrialPulseWidthEntry),
										 ventricular_amplitude=entry_to_value(self.ventricalLimitEntry),
										 ventricular_pulse_width=entry_to_value(self.ventricalPulseWidthEntry),
										 arp=entry_to_value(self.arpEntry),
										 vrp=entry_to_value(self.vrpEntry),
										 sensor_rate=entry_to_value(self.sensorRateEntry),
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

            display_error_message = not pacing_mode.validate()
        except Exception as e:
            print(e)
            display_error_message = True  # If non numerica entries

        if (display_error_message):
            self.errorLabel.config(font=(25), foreground="red")
            self.errorLabel.config(text="Invalid Entry Provided", width=33)
            # self.errorLabel.grid(row=10, column=2, columnspan=3, padx=(0, 0), pady=(0, 0), sticky=tk.E)
            self.errorLabel.place(relx=0.55, rely=0.92, anchor='sw')
        else:
            # Update saved pacing mode based on username and drop down selection
            self.user_service.update_pacing_mode(self.username, pacing_mode)

            self.errorLabel.config(text="", width=1)  # Shrink to remove, deleting wasn't working
            self.saveDeviceLabel.config(bg="green", fg="black")

            # Update displayed programmed mode
            self.currUserJson = self.load_current_user_json()
            self.actualModeLabel.config(text=self.currUserJson["pacing_mode_name"])
