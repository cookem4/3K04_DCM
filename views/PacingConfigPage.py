import tkinter as tk
from views import MainPage
from views.AppFrameBase import AppFrameBase


class PacingConfigPage(AppFrameBase):
    def __init__(self, parent):
        super().__init__(parent)
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
        self.pacingSelection.set('AOO')
        dropDownMenu = tk.OptionMenu(self, self.pacingSelection, 'AOO', 'VOO', 'AAI', 'VVI')
        dropDownMenu.config(font=(25), foreground="white", bg="black")
        dropDownMenu.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky=tk.W)

        # Sets callback listener for drop down menu
        self.pacingSelection.trace("w", self.dropDownChangeCallback)

        #########################################
        # The following show device information###
        #########################################

        self.programmedModeLabel = tk.Label(self, bg="black", text="Current Programmed Pacing Mode:")
        self.programmedModeLabel.config(font=(20), foreground="white")
        self.programmedModeLabel.grid(row=7, column=0, columnspan=2, padx=(30, 0), pady=(20, 0), sticky=tk.W)

        self.actualModeLabel = tk.Label(self, bg="black", text="VOO (test)")
        self.actualModeLabel.config(font=(20), foreground="white")
        self.actualModeLabel.grid(row=7, column=1, columnspan=1, padx=(0, 0), pady=(20, 0), sticky=tk.E)

        self.currIDLabel = tk.Label(self, bg="black", text="Connected Device ID:")
        self.currIDLabel.config(font=(20), foreground="white")
        self.currIDLabel.grid(row=8, column=0, columnspan=2, padx=(30, 0), pady=(10, 0), sticky=tk.W)

        self.currID = tk.Label(self, bg="black", text="6969420")
        self.currID.config(font=(20), foreground="white")
        self.currID.grid(row=8, column=0, columnspan=2, padx=(0, 130), pady=(10, 0), sticky=tk.E)

        self.prevIDLabel = tk.Label(self, bg="black", text="Previous Device ID:")
        self.prevIDLabel.config(font=(20), foreground="white")
        self.prevIDLabel.grid(row=9, column=0, columnspan=2, padx=(30, 0), pady=(10, 0), sticky=tk.W)

        self.prevID = tk.Label(self, bg="black", text="4206969")
        self.prevID.config(font=(20), foreground="white")
        self.prevID.grid(row=9, column=0, columnspan=2, padx=(0, 140), pady=(10, 0), sticky=tk.E)

        ###################################################################
        # The following configure the text entries for parameters
        ###################################################################

        self.lowerRateLabel = tk.Label(self, bg="black", text="Lower Rate Limit:")
        self.lowerRateLabel.config(font=(25), foreground="white")
        self.lowerRateLabel.grid(row=2, column=2, padx=(200, 0), pady=(50, 0), sticky=tk.E)

        self.lowerRateLimitEntry = tk.Entry(self, width=10, bg="white", font=(25), state='disabled')
        self.lowerRateLimitEntry.grid(row=2, column=3, pady=(50, 0), padx=(15, 0), sticky=tk.W)

        self.lowerRateUnitLabel = tk.Label(self, bg="black", text="BPM")
        self.lowerRateUnitLabel.config(font=(25), foreground="white")
        self.lowerRateUnitLabel.grid(row=2, column=3, padx=(0, 20), pady=(50, 0), sticky=tk.E)

        ############################

        self.upperRateLabel = tk.Label(self, bg="black", text="Upper Rate Limit:")
        self.upperRateLabel.config(font=(25), foreground="white")
        self.upperRateLabel.grid(row=3, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.upperRateLimitEntry = tk.Entry(self, width=10, bg="white", font=(25), state='disabled')
        self.upperRateLimitEntry.grid(row=3, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.upperRateUnitLabel = tk.Label(self, bg="black", text="BPM")
        self.upperRateUnitLabel.config(font=(25), foreground="white")
        self.upperRateUnitLabel.grid(row=3, column=3, padx=(0, 20), pady=(20, 0), sticky=tk.E)

        ############################

        self.atrialAmpLabel = tk.Label(self, bg="black", text="Atrial Amplitude:")
        self.atrialAmpLabel.config(font=(25), foreground="white")
        self.atrialAmpLabel.grid(row=4, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.atrialLimitEntry = tk.Entry(self, width=10, bg="white", font=(25), state='disabled')
        self.atrialLimitEntry.grid(row=4, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.atrialLimitUnit = tk.Label(self, bg="black", text="mV")
        self.atrialLimitUnit.config(font=(25), foreground="white")
        self.atrialLimitUnit.grid(row=4, column=3, padx=(0, 35), pady=(20, 0), sticky=tk.E)

        #############################

        self.ventricalAmpLabel = tk.Label(self, bg="black", text="Ventrical Amplitude:")
        self.ventricalAmpLabel.config(font=(25), foreground="white")
        self.ventricalAmpLabel.grid(row=5, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.ventricalLimitEntry = tk.Entry(self, width=10, bg="white", font=(25), state='disabled')
        self.ventricalLimitEntry.grid(row=5, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.ventricalLimitUnit = tk.Label(self, bg="black", text="mV")
        self.ventricalLimitUnit.config(font=(25), foreground="white")
        self.ventricalLimitUnit.grid(row=5, column=3, padx=(0, 35), pady=(20, 0), sticky=tk.E)

        ############################

        self.atrialPulseWidthLabel = tk.Label(self, bg="black", text="Atrial Pulse Width:")
        self.atrialPulseWidthLabel.config(font=(25), foreground="white")
        self.atrialPulseWidthLabel.grid(row=6, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.atrialPulseWidthEntry = tk.Entry(self, width=10, bg="white", font=(25), state='disabled')
        self.atrialPulseWidthEntry.grid(row=6, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.atrialPulseWidthUnit = tk.Label(self, bg="black", text="mSec")
        self.atrialPulseWidthUnit.config(font=(25), foreground="white")
        self.atrialPulseWidthUnit.grid(row=6, column=3, padx=(0, 15), pady=(20, 0), sticky=tk.E)

        #########################

        self.ventricalPulseWidthLabel = tk.Label(self, bg="black", text="Ventrical Pulse Width:")
        self.ventricalPulseWidthLabel.config(font=(25), foreground="white")
        self.ventricalPulseWidthLabel.grid(row=7, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.ventricalPulseWidthEntry = tk.Entry(self, width=10, bg="white", font=(25), state='disabled')
        self.ventricalPulseWidthEntry.grid(row=7, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.ventricalPulseWidthUnit = tk.Label(self, bg="black", text="mSec")
        self.ventricalPulseWidthUnit.config(font=(25), foreground="white")
        self.ventricalPulseWidthUnit.grid(row=7, column=3, padx=(0, 15), pady=(20, 0), sticky=tk.E)

        #########################

        self.arpLabel = tk.Label(self, bg="black", text="ARP:")
        self.arpLabel.config(font=(25), foreground="white")
        self.arpLabel.grid(row=8, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.arpEntry = tk.Entry(self, width=10, bg="white", font=(25), state='disabled')
        self.arpEntry.grid(row=8, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.arpUnit = tk.Label(self, bg="black", text="????")
        self.arpUnit.config(font=(25), foreground="white")
        self.arpUnit.grid(row=8, column=3, padx=(0, 15), pady=(20, 0), sticky=tk.E)

        #########################

        self.vrpLabel = tk.Label(self, bg="black", text="VRP:")
        self.vrpLabel.config(font=(25), foreground="white")
        self.vrpLabel.grid(row=9, column=2, padx=(200, 0), pady=(20, 0), sticky=tk.E)

        self.vrpEntry = tk.Entry(self, width=10, bg="white", font=(25), state='disabled')
        self.vrpEntry.grid(row=9, column=3, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.vrpUnit = tk.Label(self, bg="black", text="????")
        self.vrpUnit.config(font=(25), foreground="white")
        self.vrpUnit.grid(row=9, column=3, padx=(0, 15), pady=(20, 0), sticky=tk.E)

        #########################

        self.backBtn = tk.Button(self, text="Back", width=10, height=1, command=self.goBack)
        self.backBtn.config(font=("Helvetica", 10))
        self.backBtn.grid(row=10, column=0, columnspan=1, pady=(100, 0), padx=(15, 0), sticky=tk.W)

        self.backBtn = tk.Button(self, text="Save", width=10, height=1, command=self.saveData)
        self.backBtn.config(font=("Helvetica", 10))
        self.backBtn.grid(row=10, column=0, columnspan=1, pady=(100, 0), padx=(50, 0), sticky=tk.E)

        self.saveDeviceLabel = tk.Label(self, bg="gray", text="Saving to Device...")
        self.saveDeviceLabel.config(font=(25), foreground="white")
        self.saveDeviceLabel.grid(row=10, column=1, padx=(30, 0), pady=(100, 0), sticky=tk.W)

    def dropDownChangeCallback(self, *args):
        # Sets which boxes are grayed out based on drop down menu selection
        lowerRateLimitState = True
        upperRateLimitState = True
        atrialAmpState = True
        ventricalAmpState = True
        atrialWidthState = True
        ventricalWidthState = True
        arpState = True
        vrpState = True

        # Update variables based on drop down selection
        if self.pacingSelection.get() == "AOO":
            ventricalAmpState = False
            ventricalWidthState = False
            arpState = False
            vrpState = False
        if self.pacingSelection.get() == "VOO":
            atrialAmpState = False
            atrialWidthState = False
            arpState = False
            vrpState = False
        if self.pacingSelection.get() == "AAI":
            ventricalAmpState = False
            ventricalWidthState = False
            vrpState = False
        if self.pacingSelection.get() == "VVI":
            atrialAmpState = False
            atrialWidthState = False
            arpState = False

        get_background = lambda bool_state: "white" if bool_state else "black"
        get_state = lambda bool_state: "normal" if bool_state else "disabled"
        # Applies changes based on selected items to the entry boxes
        self.lowerRateLimitEntry.config(bg=get_background(lowerRateLimitState), state=get_state(lowerRateLimitState))
        self.upperRateLimitEntry.config(bg=get_background(upperRateLimitState), state=get_state(upperRateLimitState))
        self.atrialLimitEntry.config(bg=get_background(atrialAmpState), state=get_state(atrialAmpState))
        self.ventricalLimitEntry.config(bg=get_background(ventricalAmpState), state=get_state(ventricalAmpState))
        self.atrialPulseWidthEntry.config(bg=get_background(atrialWidthState), state=get_state(atrialWidthState))
        self.ventricalPulseWidthEntry.config(bg=get_background(ventricalWidthState),
                                             state=get_state(ventricalWidthState))
        self.arpEntry.config(bg=get_background(arpState), state=get_state(arpState))
        self.vrpEntry.config(bg=get_background(arpState), state=get_state(vrpState))

    def goBack(self):
        self.parent.switch_frame(MainPage.MainPage)

    def saveData(self):
        self.saveDeviceLabel.config(bg="green", fg="black")
