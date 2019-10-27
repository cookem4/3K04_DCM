import tkinter as tk

from main.data.PacingMode import PacingMode
from main.data.pacingmodes.AAI import AAI
from main.data.pacingmodes.AOO import AOO
from main.data.pacingmodes.VOO import VOO
from main.data.pacingmodes.VVI import VVI
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

        self.xPadding = 150

        self.connectionStateText = tk.Label(self, bg="gray", text="Connection Not Established")
        self.connectionStateText.config(font=("Helvetica", 25), foreground="white")
        self.connectionStateText.grid(row=0, column=0, columnspan=4, padx=(self.xPadding, 0), pady=(20, 0), sticky=tk.N)

        self.screenInfo = tk.Label(self, bg="light gray", text="Pacing Mode Configuration", width=50)
        self.screenInfo.config(font=("Helvetica", 30), foreground="black")
        self.screenInfo.grid(row=1, column=0, columnspan=5, padx=(60, 0), pady=(20, 0), sticky=tk.N)

        #################################################
        # The following configues the drop down menu######
        #################################################

        self.pacingModeLabel = tk.Label(self, bg="black", text="Pacing Mode:")
        self.pacingModeLabel.config(font=(25), foreground="white")
        self.pacingModeLabel.grid(row=2, column=0, padx=(0, 0), pady=(20, 0), sticky=tk.E)

        self.dropDownOptions = ['AOO', 'VOO', 'AAI', 'VVI']
        self.pacingSelection = tk.StringVar(self)
        self.pacingSelection.set(self.currUserJson["pacing_mode_name"])
        dropDownMenu = tk.OptionMenu(self, self.pacingSelection, 'AOO', 'VOO', 'AAI', 'VVI')
        dropDownMenu.config(font=(25), foreground="white", bg="black")
        dropDownMenu.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky=tk.W)

        # Sets callback listener for drop down menu
        self.pacingSelection.trace("w", self.drop_down_callback)

        #########################################
        # The following show device information###
        #########################################

        self.programmedModeLabel = tk.Label(self, bg="black", text="Current Programmed Pacing Mode:")
        self.programmedModeLabel.config(font=(20), foreground="white")
        self.programmedModeLabel.grid(row=7, column=0, columnspan=2, padx=(30, 0), pady=(20, 0), sticky=tk.W)

        self.actualModeLabel = tk.Label(self, bg="black", text=self.currUserJson["pacing_mode_name"])
        self.actualModeLabel.config(font=(20), foreground="white")
        self.actualModeLabel.grid(row=7, column=1, columnspan=1, padx=(0, 75), pady=(20, 0), sticky=tk.E)

        self.currIDLabel = tk.Label(self, bg="black", text="Connected Device ID:")
        self.currIDLabel.config(font=(20), foreground="white")
        self.currIDLabel.grid(row=8, column=0, columnspan=2, padx=(30, 0), pady=(10, 0), sticky=tk.W)

        self.currID = tk.Label(self, bg="black", text="123456")
        self.currID.config(font=(20), foreground="white")
        self.currID.grid(row=8, column=0, columnspan=2, padx=(0, 130), pady=(10, 0), sticky=tk.E)

        self.prevIDLabel = tk.Label(self, bg="black", text="Previous Device ID:")
        self.prevIDLabel.config(font=(20), foreground="white")
        self.prevIDLabel.grid(row=9, column=0, columnspan=2, padx=(30, 0), pady=(10, 0), sticky=tk.W)

        self.prevID = tk.Label(self, bg="black", text="654321")
        self.prevID.config(font=(20), foreground="white")
        self.prevID.grid(row=9, column=0, columnspan=2, padx=(0, 140), pady=(10, 0), sticky=tk.E)

        ###################################################################
        # The following configure the text entries for parameters
        ###################################################################

        self.lowerRateLabel = tk.Label(self, bg="black", text="Lower Rate Limit:")
        self.lowerRateLabel.config(font=(25), foreground="white")
        self.lowerRateLabel.grid(row=2, column=2, padx=(200, 0), pady=(50, 0), sticky=tk.E)

        self.lowerRateLimitEntry = tk.Entry(self, textvariable=self.usrLowerRateLimit, width=10, font=(25),
                                            bg=self.enabled_bg,
                                            disabledbackground=self.disabled_bg)
        self.lowerRateLimitEntry.grid(row=2, column=3, pady=(50, 0), padx=(15, 0), sticky=tk.W)

        self.lowerRateUnitLabel = tk.Label(self, bg="black", text="ppm")
        self.lowerRateUnitLabel.config(font=(25), foreground="white")
        self.lowerRateUnitLabel.grid(row=2, column=3, padx=(0, 20), pady=(50, 0), sticky=tk.E)

        ############################

        self.upperRateLabel = tk.Label(self, bg="black", text="Upper Rate Limit:")
        self.upperRateLabel.config(font=(25), foreground="white")
        self.upperRateLabel.grid(row=3, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.upperRateLimitEntry = tk.Entry(self, textvariable=self.usrUpperRateLimit, width=10, font=(25),
                                            bg=self.enabled_bg,
                                            disabledbackground=self.disabled_bg)
        self.upperRateLimitEntry.grid(row=3, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.upperRateUnitLabel = tk.Label(self, bg="black", text="ppm")
        self.upperRateUnitLabel.config(font=(25), foreground="white")
        self.upperRateUnitLabel.grid(row=3, column=3, padx=(0, 20), pady=(20, 0), sticky=tk.E)

        ############################

        self.atrialAmpLabel = tk.Label(self, bg="black", text="Atrial Amplitude:")
        self.atrialAmpLabel.config(font=(25), foreground="white")
        self.atrialAmpLabel.grid(row=4, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.atrialLimitEntry = tk.Entry(self, textvariable=self.usrAtrialAmp, width=10, font=(25), bg=self.enabled_bg,
                                         disabledbackground=self.disabled_bg)
        self.atrialLimitEntry.grid(row=4, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.atrialLimitUnit = tk.Label(self, bg="black", text="V")
        self.atrialLimitUnit.config(font=(25), foreground="white")
        self.atrialLimitUnit.grid(row=4, column=3, padx=(0, 35), pady=(20, 0), sticky=tk.E)

        #############################

        self.ventricalAmpLabel = tk.Label(self, bg="black", text="Ventricular Amplitude:")
        self.ventricalAmpLabel.config(font=(25), foreground="white")
        self.ventricalAmpLabel.grid(row=5, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.ventricalLimitEntry = tk.Entry(self, textvariable=self.usrVentricalAmp, width=10, font=(25),
                                            bg=self.enabled_bg,
                                            disabledbackground=self.disabled_bg)
        self.ventricalLimitEntry.grid(row=5, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.ventricalLimitUnit = tk.Label(self, bg="black", text="V")
        self.ventricalLimitUnit.config(font=(25), foreground="white")
        self.ventricalLimitUnit.grid(row=5, column=3, padx=(0, 35), pady=(20, 0), sticky=tk.E)

        ############################

        self.atrialPulseWidthLabel = tk.Label(self, bg="black", text="Atrial Pulse Width:")
        self.atrialPulseWidthLabel.config(font=25, foreground="white")
        self.atrialPulseWidthLabel.grid(row=6, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.atrialPulseWidthEntry = tk.Entry(self, textvariable=self.usrAtrialPulseWidth, width=10, font=25,
                                              bg=self.enabled_bg,
                                              disabledbackground=self.disabled_bg)
        self.atrialPulseWidthEntry.grid(row=6, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.atrialPulseWidthUnit = tk.Label(self, bg="black", text="mSec")
        self.atrialPulseWidthUnit.config(font=(25), foreground="white")
        self.atrialPulseWidthUnit.grid(row=6, column=3, padx=(0, 15), pady=(20, 0), sticky=tk.E)

        #########################

        self.ventricalPulseWidthLabel = tk.Label(self, bg="black", text="Ventricular Pulse Width:")
        self.ventricalPulseWidthLabel.config(font=25, foreground="white")
        self.ventricalPulseWidthLabel.grid(row=7, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.ventricalPulseWidthEntry = tk.Entry(self, textvariable=self.usrVentricalPulseWidth, width=10, font=(25),
                                                 bg=self.enabled_bg,
                                                 disabledbackground=self.disabled_bg)
        self.ventricalPulseWidthEntry.grid(row=7, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.ventricalPulseWidthUnit = tk.Label(self, bg="black", text="mSec")
        self.ventricalPulseWidthUnit.config(font=(25), foreground="white")
        self.ventricalPulseWidthUnit.grid(row=7, column=3, padx=(0, 15), pady=(20, 0), sticky=tk.E)

        #########################

        self.arpLabel = tk.Label(self, bg="black", text="ARP:")
        self.arpLabel.config(font=(25), foreground="white")
        self.arpLabel.grid(row=8, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.arpEntry = tk.Entry(self, textvariable=self.usrARP, width=10, font=(25), bg=self.enabled_bg,
                                 disabledbackground=self.disabled_bg)
        self.arpEntry.grid(row=8, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.arpUnit = tk.Label(self, bg="black", text="mSec")
        self.arpUnit.config(font=(25), foreground="white")
        self.arpUnit.grid(row=8, column=3, padx=(0, 10), pady=(20, 0), sticky=tk.E)

        #########################

        self.vrpLabel = tk.Label(self, bg="black", text="VRP:")
        self.vrpLabel.config(font=(25), foreground="white")
        self.vrpLabel.grid(row=9, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.vrpEntry = tk.Entry(self, textvariable=self.usrVRP, width=10, font=(25), bg=self.enabled_bg,
                                 disabledbackground=self.disabled_bg)
        self.vrpEntry.grid(row=9, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.vrpUnit = tk.Label(self, bg="black", text="mSec")
        self.vrpUnit.config(font=(25), foreground="white")
        self.vrpUnit.grid(row=9, column=3, padx=(0, 10), pady=(20, 0), sticky=tk.E)

        #########################

        self.backBtn = tk.Button(self, text="Back", width=10, height=1, command=self.go_back)
        self.backBtn.config(font=("Helvetica", 10))
        self.backBtn.grid(row=10, column=0, columnspan=1, pady=(100, 0), padx=(15, 0), sticky=tk.W)

        self.backBtn = tk.Button(self, text="Save", width=10, height=1, command=self.save_data)
        self.backBtn.config(font=("Helvetica", 10))
        self.backBtn.grid(row=10, column=0, columnspan=1, pady=(100, 0), padx=(50, 0), sticky=tk.E)

        self.saveDeviceLabel = tk.Label(self, bg="gray", text="Saving to Device...")
        self.saveDeviceLabel.config(font=(25), foreground="white")
        self.saveDeviceLabel.grid(row=10, column=1, padx=(30, 0), pady=(100, 0), sticky=tk.W)

        self.errorLabel = tk.Label(self, bg="black", text="Erroneous Parameters Provided", width=33)

        self.drop_down_callback()

        # Set textbox values based on user profile
        # String slicing of json object
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
                       "pacing_mode_settings"].index("}")]
        self.usrLowerRateLimit.set("" if (lowerRateLimitSlice == "null") else (lowerRateLimitSlice))
        self.usrUpperRateLimit.set("" if (upperRateLimitSlice == "null") else upperRateLimitSlice)
        self.usrAtrialAmp.set("" if (atrialAmpSlice == "null") else atrialAmpSlice)
        self.usrAtrialPulseWidth.set("" if (atrialPulseWidthSlice == "null") else atrialPulseWidthSlice)
        self.usrVentricalAmp.set("" if (ventricalAmpSlice == "null") else ventricalAmpSlice)
        self.usrVentricalPulseWidth.set("" if (ventricalPulseWidthSlice == "null") else ventricalPulseWidthSlice)
        self.usrARP.set("" if (arpSlice == "null") else arpSlice)
        self.usrVRP.set("" if (vrpSlice == "null") else vrpSlice)

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

        # Sets which boxes are grayed out based on drop down menu selection
        # Update variables based on drop down selection
        if self.pacingSelection.get() == "AOO":
            self.set_states(VLE="disabled", VPW="disabled", ARP="disabled", VRP="disabled")
        if self.pacingSelection.get() == "VOO":
            self.set_states(ALE="disabled", APW="disabled", ARP="disabled", VRP="disabled")
        if self.pacingSelection.get() == "AAI":
            self.set_states(VLE="disabled", VPW="disabled", VRP="disabled")
        if self.pacingSelection.get() == "VVI":
            self.set_states(ALE="disabled", APW="disabled", ARP="disabled")

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
            # Catch boundary cases from erroneous text box entries
            pacing_mode: PacingMode = PacingMode(lower_rate_limit=entry_to_value(self.lowerRateLimitEntry),
                                                 upper_rate_limit=entry_to_value(self.upperRateLimitEntry),
                                                 atrial_amplitude=entry_to_value(self.atrialLimitEntry),
                                                 atrial_pulse_width=entry_to_value(self.atrialPulseWidthEntry),
                                                 ventricular_amplitude=entry_to_value(self.ventricalLimitEntry),
                                                 ventricular_pulse_width=entry_to_value(self.ventricalPulseWidthEntry),
                                                 arp=entry_to_value(self.arpEntry),
                                                 vrp=entry_to_value(self.vrpEntry))
        
            if self.pacingSelection.get() == "AOO":
                pacing_mode.__class__ = AOO
            if self.pacingSelection.get() == "VOO":
                pacing_mode.__class__ = VOO
            if self.pacingSelection.get() == "AAI":
                pacing_mode.__class__ = AAI
            if self.pacingSelection.get() == "VVI":
                pacing_mode.__class__ = VVI

            display_error_message = not pacing_mode.validate()
        except Exception as e:
            print(e)
            display_error_message = True  # If non numerica entries

        if (display_error_message):
            self.errorLabel.config(font=(25), foreground="red")
            self.errorLabel.config(text="Invalid Entry Provided", width=33)
            self.errorLabel.grid(row=10, column=2, columnspan=3, padx=(0, 0), pady=(0, 0), sticky=tk.E)
        else:
            # Update saved pacing mode based on username and drop down selection
            self.user_service.update_pacing_mode(self.username, pacing_mode)

            self.errorLabel.config(text="", width=1)  # Shrink to remove, deleting wasn't working
            self.saveDeviceLabel.config(bg="green", fg="black")

            # Update displayed programmed mode
            self.currUserJson = self.load_current_user_json()
            self.actualModeLabel.config(text=self.currUserJson["pacing_mode_name"])
