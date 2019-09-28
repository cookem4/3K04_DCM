import tkinter as tk


class DCM_GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()

class NewUserPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(background="black")
        self.parent = parent
        self.width= 1280
        self.height = 720
        self.xPadding = 450
    
        self.newUserText = tk.Label(self, bg="black", text = "Please enter your new\nusername and password")
        self.newUserText.config(font = ("Helvetica", 30), foreground = "white")
        self.newUserText.grid(row = 0, column = 0, columnspan = 2, padx = (self.xPadding,0), pady = (200,75), sticky = tk.N)

        self.userName = tk.Label(self, bg="black", text = "Username:")
        self.userName.config(font=(25), foreground = "white")
        self.userName.grid(row = 1, column = 0, padx = (self.xPadding,0), pady = (0,0), sticky = tk.E)

        self.passsord = tk.Label(self,  bg="black",text = "Password:")
        self.passsord.config(font=(25), foreground = "white")
        self.passsord.grid(row = 2, column = 0, padx = (self.xPadding,0), pady = (20,0), sticky = tk.E)

        self.passsord = tk.Label(self, bg="black", text = "Confirm Password:")
        self.passsord.config(font=(25), foreground = "white")
        self.passsord.grid(row = 3, column = 0, padx = (self.xPadding,0), pady = (20,0), sticky = tk.E)

        self.usernameEntry = tk.Entry(self, width=20, bg = "white", font = (25))
        self.usernameEntry.grid(row = 1, column = 1, pady = (0,0), padx = (0, 0), sticky = tk.SW)

        self.passwordEntry = tk.Entry(self, width=20, bg = "white", font = (25))
        self.passwordEntry.grid(row = 2, column = 1,pady = (0,0), padx = (0, 0), sticky = tk.SW)

        self.confirmPassword = tk.Entry(self, width=20, bg = "white", font = (25))
        self.confirmPassword.grid(row = 3, column = 1,pady = (0,0), padx = (0, 0), sticky = tk.SW)

        self.newAccountButton = tk.Button(self, text = "Register", width = 20, command = self.registerUser)
        self.newAccountButton.grid(row = 4, column = 0, columnspan = 2, pady = (50,0), padx = (self.xPadding,0),sticky = tk.N)
        
    def registerUser(self):
        self.parent.switch_frame(LoginPage)

        
class MainPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(background="black")
        self.parent = parent
        self.width= 1280
        self.height = 720
    
        self.connectionStateText = tk.Label(self, bg="gray", text = "Connection Not Established")
        self.connectionStateText.config(font = ("Helvetica", 25), foreground = "white")
        self.connectionStateText.grid(row = 0, column = 0, columnspan = 4, padx = (0,0), pady = (20,0), sticky = tk.N)

        self.screenInfo = tk.Label(self, bg="light gray", text = "HOME", width = 48)
        self.screenInfo.config(font = ("Helvetica", 35), foreground = "black")
        self.screenInfo.grid(row = 1, column = 0, columnspan = 3, padx = (0, 0), pady = (20,0), sticky = tk.N)

        self.editPacingButton = tk.Button(self, text = "Edit Pacing Mode\nand Parameters", width = 20, height = 6, command = self.editPacingModes)
        self.editPacingButton.config(font = ("Helvetica", 20))
        self.editPacingButton.grid(row = 5, column = 0, columnspan = 3, pady = (50,0), padx = (45,0),sticky = tk.NW)

        self.viewCurrEGM = tk.Button(self, text = "View Current EGM\nData", width = 20, height = 6, command = self.viewCurrEGMDat)
        self.viewCurrEGM.config(font = ("Helvetica", 20))
        self.viewCurrEGM.grid(row = 5, column = 0, columnspan = 3, pady = (50,0), padx = (0,0),sticky = tk.N)

        self.viewPastEGM = tk.Button(self, text = "View Past EGM\nData", width = 20, height = 6, command = self.viewPastEGMDat)
        self.viewPastEGM.config(font = ("Helvetica", 20))
        self.viewPastEGM.grid(row = 5, column = 0, columnspan = 3, pady = (50,0), padx = (0,60),sticky = tk.NE)

        self.logoutBtn = tk.Button(self, text = "Logout", width = 12, height = 2, command = self.logout)
        self.logoutBtn.config(font = ("Helvetica", 12))
        self.logoutBtn.grid(row = 6, column = 0, columnspan = 1, pady = (125,0), padx = (10,0),sticky = tk.W)

        #########################################
        #The following show device information###
        #########################################

        self.programmedModeLabel = tk.Label(self,  bg="black",text = "Current Programmed Pacing Mode: VOO (test)")
        self.programmedModeLabel.config(font=(15), foreground = "white")
        self.programmedModeLabel.grid(row = 2, column = 0, columnspan = 3, padx = (0,0), pady = (30,0), sticky = tk.N)

        self.currIDLabel = tk.Label(self,  bg="black",text = "Connected Device ID: 6969420")
        self.currIDLabel.config(font=(15), foreground = "white")
        self.currIDLabel.grid(row = 3, column = 0, columnspan = 3, padx = (0,0), pady = (0,0), sticky = tk.N)

        self.prevIDLabel = tk.Label(self,  bg="black",text = "Previous Device ID: 4206969")
        self.prevIDLabel.config(font=(15), foreground = "white")
        self.prevIDLabel.grid(row = 4, column = 0, columnspan = 3, padx = (0,0), pady = (0,0), sticky = tk.N)


    def editPacingModes(self):
        self.parent.switch_frame(PacingConfig)
    def viewCurrEGMDat(self):
        print("Present Data")
    def viewPastEGMDat(self):
        print("Past Data")
    def logout(self):
        self.parent.switch_frame(LoginPage)

class PacingConfig(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(background="black")
        self.parent = parent
        self.width= 1280
        self.height = 720
        self.xPadding = 150

        self.connectionStateText = tk.Label(self, bg="gray", text = "Connection Not Established")
        self.connectionStateText.config(font = ("Helvetica", 25), foreground = "white")
        self.connectionStateText.grid(row = 0, column = 0, columnspan = 4, padx = (self.xPadding,0), pady = (20,0), sticky = tk.N)

        self.screenInfo = tk.Label(self, bg="light gray", text = "Pacing Mode Configuration", width = 50)
        self.screenInfo.config(font = ("Helvetica", 30), foreground = "black")
        self.screenInfo.grid(row = 1, column = 0, columnspan = 5, padx = (60,0), pady = (20,0), sticky = tk.N)


        #################################################
        #The following configues the drop down menu######
        #################################################

        self.pacingModeLabel = tk.Label(self,  bg="black",text = "Pacing Mode:")
        self.pacingModeLabel.config(font=(25), foreground = "white")
        self.pacingModeLabel.grid(row = 2, column = 0, padx = (0,0), pady = (20,0), sticky = tk.E)


        self.dropDownOptions = ['AOO', 'VOO', 'AAI', 'VVI']
        self.pacingSelection = tk.StringVar(self)
        self.pacingSelection.set('AOO')
        dropDownMenu = tk.OptionMenu(self, self.pacingSelection, 'AOO', 'VOO', 'AAI', 'VVI')
        dropDownMenu.config(font=(25), foreground = "white", bg = "black")
        dropDownMenu.grid(row = 2, column = 1, padx = (20,0), pady = (20,0), sticky = tk.W)

        #Sets callback listener for drop down menu
        self.pacingSelection.trace("w", self.dropDownChangeCallback)

        

        #########################################
        #The following show device information###
        #########################################

        self.programmedModeLabel = tk.Label(self,  bg="black",text = "Current Programmed Pacing Mode:")
        self.programmedModeLabel.config(font=(20), foreground = "white")
        self.programmedModeLabel.grid(row = 7, column = 0, columnspan = 2, padx = (30,0), pady = (20,0), sticky = tk.W)

        self.actualModeLabel = tk.Label(self,  bg="black",text = "VOO (test)")
        self.actualModeLabel.config(font=(20), foreground = "white")
        self.actualModeLabel.grid(row = 7, column = 1, columnspan = 1, padx = (0,0), pady = (20,0), sticky = tk.E)

        self.currIDLabel = tk.Label(self,  bg="black",text = "Connected Device ID:")
        self.currIDLabel.config(font=(20), foreground = "white")
        self.currIDLabel.grid(row = 8, column = 0, columnspan = 2, padx = (30,0), pady = (10,0), sticky = tk.W)

        self.currID = tk.Label(self,  bg="black",text = "6969420")
        self.currID.config(font=(20), foreground = "white")
        self.currID.grid(row = 8, column = 0, columnspan = 2, padx = (0,130), pady = (10,0), sticky = tk.E)

        self.prevIDLabel = tk.Label(self,  bg="black",text = "Previous Device ID:")
        self.prevIDLabel.config(font=(20), foreground = "white")
        self.prevIDLabel.grid(row = 9, column = 0, columnspan = 2, padx = (30,0), pady = (10,0), sticky = tk.W)

        self.prevID = tk.Label(self,  bg="black",text = "4206969")
        self.prevID.config(font=(20), foreground = "white")
        self.prevID.grid(row = 9, column = 0, columnspan = 2, padx = (0,140), pady = (10,0), sticky = tk.E)

        ###################################################################
        #The following configure the text entries for parameters
        ################################################################### 

        self.lowerRateLabel = tk.Label(self,  bg="black",text = "Lower Rate Limit:")
        self.lowerRateLabel.config(font=(25), foreground = "white")
        self.lowerRateLabel.grid(row = 2, column = 2, padx = (200,0), pady = (50,0), sticky = tk.E)

        self.lowerRateLimitEntry = tk.Entry(self, width=10, bg = "white", font = (25), state = 'disabled')
        self.lowerRateLimitEntry.grid(row = 2, column = 3, pady = (50,0), padx = (15, 0), sticky = tk.W)

        self.lowerRateUnitLabel = tk.Label(self,  bg="black",text = "BPM")
        self.lowerRateUnitLabel.config(font=(25), foreground = "white")
        self.lowerRateUnitLabel.grid(row = 2, column = 3, padx = (0,20), pady = (50,0), sticky = tk.E)

        ############################

        self.upperRateLabel = tk.Label(self,  bg="black",text = "Upper Rate Limit:")
        self.upperRateLabel.config(font=(25), foreground = "white")
        self.upperRateLabel.grid(row = 3, column = 2, padx = (200,0), pady = (20,0), sticky = tk.E)

        self.upperRateLimitEntry = tk.Entry(self, width=10, bg = "white", font = (25), state = 'disabled')
        self.upperRateLimitEntry.grid(row = 3, column = 3, pady = (20,0), padx = (15, 0), sticky = tk.W)

        self.upperRateUnitLabel = tk.Label(self,  bg="black",text = "BPM")
        self.upperRateUnitLabel.config(font=(25), foreground = "white")
        self.upperRateUnitLabel.grid(row = 3, column = 3, padx = (0,20), pady = (20,0), sticky = tk.E)

        ############################

        self.atrialAmpLabel = tk.Label(self,  bg="black",text = "Atrial Amplitude:")
        self.atrialAmpLabel.config(font=(25), foreground = "white")
        self.atrialAmpLabel.grid(row = 4, column = 2, padx = (200,0), pady = (20,0), sticky = tk.E)

        self.atrialLimitEntry = tk.Entry(self, width=10, bg = "white", font = (25), state = 'disabled')
        self.atrialLimitEntry.grid(row = 4, column = 3, pady = (20,0), padx = (15, 0), sticky = tk.W)

        self.atrialLimitUnit = tk.Label(self,  bg="black",text = "mV")
        self.atrialLimitUnit.config(font=(25), foreground = "white")
        self.atrialLimitUnit.grid(row = 4, column = 3, padx = (0,35), pady = (20,0), sticky = tk.E)

        #############################

        self.ventricalAmpLabel = tk.Label(self,  bg="black",text = "Ventrical Amplitude:")
        self.ventricalAmpLabel.config(font=(25), foreground = "white")
        self.ventricalAmpLabel.grid(row = 5, column = 2, padx = (200,0), pady = (20,0), sticky = tk.E)

        self.ventricalLimitEntry = tk.Entry(self, width=10, bg = "white", font = (25), state = 'disabled')
        self.ventricalLimitEntry.grid(row = 5, column = 3, pady = (20,0), padx = (15, 0), sticky = tk.W)

        self.ventricalLimitUnit = tk.Label(self,  bg="black",text = "mV")
        self.ventricalLimitUnit.config(font=(25), foreground = "white")
        self.ventricalLimitUnit.grid(row = 5, column = 3, padx = (0,35), pady = (20,0), sticky = tk.E)


        ############################

        self.atrialPulseWidthLabel = tk.Label(self,  bg="black",text = "Atrial Pulse Width:")
        self.atrialPulseWidthLabel.config(font=(25), foreground = "white")
        self.atrialPulseWidthLabel.grid(row = 6, column = 2, padx = (200,0), pady = (20,0), sticky = tk.E)

        self.atrialPulseWidthEntry = tk.Entry(self, width=10, bg = "white", font = (25), state = 'disabled')
        self.atrialPulseWidthEntry.grid(row = 6, column = 3, pady = (20,0), padx = (15, 0), sticky = tk.W)

        self.atrialPulseWidthUnit = tk.Label(self,  bg="black",text = "mSec")
        self.atrialPulseWidthUnit.config(font=(25), foreground = "white")
        self.atrialPulseWidthUnit.grid(row = 6, column = 3, padx = (0,15), pady = (20,0), sticky = tk.E)

        #########################

        self.ventricalPulseWidthLabel = tk.Label(self,  bg="black",text = "Ventrical Pulse Width:")
        self.ventricalPulseWidthLabel.config(font=(25), foreground = "white")
        self.ventricalPulseWidthLabel.grid(row = 7, column = 2, padx = (200,0), pady = (20,0), sticky = tk.E)

        self.ventricalPulseWidthEntry = tk.Entry(self, width=10, bg = "white", font = (25), state = 'disabled')
        self.ventricalPulseWidthEntry.grid(row = 7, column = 3, pady = (20,0), padx = (15, 0), sticky = tk.W)

        self.ventricalPulseWidthUnit = tk.Label(self,  bg="black",text = "mSec")
        self.ventricalPulseWidthUnit.config(font=(25), foreground = "white")
        self.ventricalPulseWidthUnit.grid(row = 7, column = 3, padx = (0,15), pady = (20,0), sticky = tk.E)

        #########################

        self.arpLabel = tk.Label(self,  bg="black",text = "ARP:")
        self.arpLabel.config(font=(25), foreground = "white")
        self.arpLabel.grid(row = 8, column = 2, padx = (200,0), pady = (20,0), sticky = tk.E)

        self.arpEntry = tk.Entry(self, width=10, bg = "white", font = (25), state = 'disabled')
        self.arpEntry.grid(row = 8, column = 3, pady = (20,0), padx = (15, 0), sticky = tk.W)

        self.arpUnit = tk.Label(self,  bg="black",text = "????")
        self.arpUnit.config(font=(25), foreground = "white")
        self.arpUnit.grid(row = 8, column = 3, padx = (0,15), pady = (20,0), sticky = tk.E)

        #########################

        self.vrpLabel = tk.Label(self,  bg="black",text = "VRP:")
        self.vrpLabel.config(font=(25), foreground = "white")
        self.vrpLabel.grid(row = 9, column = 2, padx = (200,0), pady = (20,0), sticky = tk.E)

        self.vrpEntry = tk.Entry(self, width=10, bg = "white", font = (25), state = 'disabled')
        self.vrpEntry.grid(row = 9, column = 3, pady = (20,0), padx = (15, 0), sticky = tk.W)

        self.vrpUnit = tk.Label(self,  bg="black",text = "????")
        self.vrpUnit.config(font=(25), foreground = "white")
        self.vrpUnit.grid(row = 9, column = 3, padx = (0,15), pady = (20,0), sticky = tk.E)

        #########################


        self.backBtn = tk.Button(self, text = "Back", width = 10, height = 1, command = self.goBack)
        self.backBtn.config(font = ("Helvetica", 10))
        self.backBtn.grid(row =10, column = 0, columnspan = 1, pady = (100,0), padx = (15,0),sticky = tk.W)

        self.backBtn = tk.Button(self, text = "Save", width = 10, height = 1, command = self.saveData)
        self.backBtn.config(font = ("Helvetica", 10))
        self.backBtn.grid(row = 10, column = 0, columnspan = 1, pady = (100,0), padx = (50,0),sticky = tk.E)

        self.saveDeviceLabel = tk.Label(self,  bg="gray",text = "Saving to Device...")
        self.saveDeviceLabel.config(font=(25), foreground = "white")
        self.saveDeviceLabel.grid(row = 10, column = 1, padx = (30,0), pady = (100,0), sticky = tk.W)

    def dropDownChangeCallback(self, *args):
        #Sets which boxes are grayed out based on drop down menu selection
        lowerRateLimitBack = "white"
        upperRateLimitBack = "white"
        atrialAmpBack = "white"
        ventricalAmpBack = "white"
        atrialWidthBack = "white"
        ventricalWidthBack = "white"
        arpBack = "white"
        vrpBack = "white"
        lowerRateLimitState = 'normal'
        upperRateLimitState = 'normal'
        atrialAmpState = 'normal'
        ventricalAmpState = 'normal'
        atrialWidthState= 'normal'
        ventricalWidthState = 'normal'
        arpState = 'normal'
        vrpState = 'normal'
        if(self.pacingSelection.get() == "AOO"):
            ventricalAmpBack = "gray"
            ventricalWidthBack = "gray"
            arpBack = "gray"
            vrpBack = "gray"
            ventricalAmpState = 'disabled'
            ventricalWidthState = 'disabled'
            arpState = 'disabled'
            vrpState = 'disabled'
        if(self.pacingSelection.get() == "VOO"):
            atrialAmpBack = "gray"
            atrialWidthBack = "gray"
            arpBack = "gray"
            vrpBack = "gray"
            atrialAmpState = 'disabled'
            atrialWidthState = 'disabled'
            arpState = 'disabled'
            vrpState = 'disabled'
        if(self.pacingSelection.get() == "AAI"):
            ventricalAmpBack = "gray"
            ventricalWidthBack = "gray"
            vrpBack = "gray"
            ventricalAmpState = 'disabled'
            ventricalWidthState = 'disabled'
            vrpState = 'disabled'
        if(self.pacingSelection.get() == "VVI"):
            atrialAmpBack = "gray"
            atrialWidthBack = "gray"
            arpBack = "gray"
            atrialAmpState = 'disabled'
            atrialWidthState = 'disabled'
            arpState = 'disabled'

        self.lowerRateLimitEntry.config(bg = lowerRateLimitBack, state = lowerRateLimitState)
        self.upperRateLimitEntry.config(bg = upperRateLimitBack, state = upperRateLimitState)
        self.atrialLimitEntry.config(bg = atrialAmpBack, state = atrialAmpState)
        self.ventricalLimitEntry.config(bg = ventricalAmpBack, state = ventricalAmpState)
        self.atrialPulseWidthEntry.config(bg = atrialWidthBack, state = atrialWidthState)
        self.ventricalPulseWidthEntry.config(bg = ventricalWidthBack, state = ventricalWidthState)
        self.arpEntry.config(bg = arpBack, state = arpState)
        self.vrpEntry.config(bg = vrpBack, state = vrpState)
    def goBack(self):
        self.parent.switch_frame(MainPage)
    def saveData(self):
        self.saveDeviceLabel.config(bg = "green", fg = "black")

        
class LoginPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.title("DCM")
        self.configure(background="black")
        parent.configure(background="black")
        parent.geometry("1280x720")
        self.width= 1280
        self.height = 720
        self.xPadding = 325
        
        self.welcomeText = tk.Label(self, bg="black", text = "Welcome to the Pacemaker DCM\n This tool allows a pacemaker to be configured in the \n AOO, VOO, AAI, and VVI pacing modes")
        self.welcomeText.config(font=("Helvetica",20), foreground = "white")
        self.welcomeText.grid(row = 0, column = 0, columnspan = 2, padx = (self.xPadding,0), pady = (200,75), sticky = tk.N)
        
        self.badLoginText = tk.Label(self, bg="black", text = "INCORRECT USERNAME OR PASSWORD")
        self.badLoginText.configure(font=(50), foreground = "red")

        self.userName = tk.Label(self,  bg="black",text = "Username:")
        self.userName.config(font=(25), foreground = "white")
        self.userName.grid(row = 1, column = 0, padx = (self.xPadding,0), pady = (20,0), sticky = tk.E)

        self.passsord = tk.Label(self, bg="black", text = "Password:")
        self.passsord.config(font=(25), foreground = "white")
        self.passsord.grid(row = 2, column = 0, padx = (self.xPadding,0), pady = (20,0), sticky = tk.E)

        self.usernameEntry = tk.Entry(self, width=20, bg = "white", font = (25))
        self.usernameEntry.grid(row = 1, column = 1, pady = (0,0), padx = (0, 0), sticky = tk.SW)

        self.passwordEntry = tk.Entry(self, width=20, bg = "white", font = (25))
        self.passwordEntry.grid(row = 2, column = 1,pady = (0,0), padx = (0, 0), sticky = tk.SW)

        self.loginButton = tk.Button(self, text = "Login", width = 10, command = self.loginBtn)
        self.loginButton.grid(row = 3, column = 0, columnspan = 2, pady = (25,0), padx = (self.xPadding,0),sticky = tk.N)

        self.newAccountButton = tk.Button(self, text = "Create New Account", width = 20, command = lambda: parent.switch_frame(NewUserPage))
        self.newAccountButton.grid(row = 4, column = 0, columnspan = 2, pady = (25,0), padx = (self.xPadding,0),sticky = tk.N)
        
    def loginBtn(self):
        if(True):
            self.parent.switch_frame(MainPage)
        else:
            self.badLoginText.grid(row = 0, column = 0, columnspan = 2, padx = (self.xPadding,0), pady = (325,0), sticky = tk.N) 

        

if __name__ == "__main__":
    app = DCM_GUI()
    app.mainloop()
