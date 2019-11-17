import tkinter as tk

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from main.views import MainPage
from main.views.AppFrameBase import AppFrameBase
from threading import Thread
import time
matplotlib.use("TkAgg")
import math

class EGMDataPage(AppFrameBase):

    def __init__(self, parent):
        super().__init__(parent)

        self.username = self.session_service.get().username

        self.currUserJson = self.load_current_user_json()

        # The following are temporary values that are graphed when the drop down menu changes
        # Based on what drop down menu selection is chosen, this list will be indexed differently
        # This list will constantly be udpated from the serial module
        # First index is atrial pacing second is ventricle pacing
        #self.setToGraph = [[5, 6, 1, 3, 8, 9, 3, 5, 5, 6, 1, 3, 8, 9, 3, 5],
                          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 14, 15, 16]]
        self.setToGraph = [[0],[0]]
        self.addCntr = 0

        self.connectionStateText = tk.Label(self, bg="gray", text="Connection Not Established")
        self.connectionStateText.config(font=("Helvetica", 25), foreground="black")
        self.connectionStateText.grid(row=0, column=0, columnspan=3, padx=(90, 0), pady=(20, 0), sticky=tk.N)

        self.screenInfo = tk.Label(self, bg="light gray", text="EGM Data", width=50)
        self.screenInfo.config(font=("Helvetica", 30), foreground="black")
        self.screenInfo.grid(row=1, column=0, columnspan=3, padx=(60, 0), pady=(20, 0), sticky=tk.N)

        self.backBtn = tk.Button(self, text="Back", width=10, height=2, command=self.go_back)
        self.backBtn.config(font=("Helvetica", 10))
        self.backBtn.grid(row=4, column=0, columnspan=1, pady=(20, 0), padx=(15, 0), sticky=tk.W)

        self.startBtn = tk.Button(self, text="Start", width=8, height=1, command=self.toggleGraphing)
        self.startBtn.config(state = tk.DISABLED)
        self.startBtn.config(font=("Helvetica", 10))
        self.startBtn.grid(row=2, column=1, columnspan=1, pady=(20, 0), padx=(150, 0), sticky=tk.W)
        self.graphingEnabled = False

        self.displayModeLabel = tk.Label(self, bg="black", text="Display Mode:")
        self.displayModeLabel.config(font=(25), foreground="white")
        self.displayModeLabel.grid(row=2, column=0, padx=(270, 0), pady=(20, 0), sticky=tk.E)

        self.dropDownOptions = ['Atrium', 'Ventrical', 'Both']
        self.displaySelection = tk.StringVar(self)
        self.displaySelection.set('Atrium')
        dropDownMenu = tk.OptionMenu(self, self.displaySelection, 'Atrium', 'Ventrical', 'Both')
        dropDownMenu.config(font=(25), foreground="white", bg="black")
        dropDownMenu.grid(row=2, column=1, padx=(0, 0), pady=(20, 0), sticky=tk.W)

        # Sets callback listener for drop down menu
        self.displaySelection.trace("w", self.drop_down_callback)

        ##############################################
        #### The following creates a graph ###########
        ##############################################

        f = Figure(figsize=(10, 4), dpi=100)
        self.a = f.add_subplot(111)
        self.a.plot([0], [0])
        # a.title("EGM Data for Device 123345")
        # a.xlabel("Time (s)")
        # a.ylabel("Voltage")

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=0, columnspan=3, padx=(135, 0), pady=(30, 0), sticky=tk.W)

        #Setup labels based on pacing status
        if self.serial_indicators.isConnected():
            self.connectionStateText.config(text="Connection Established", foreground="white", background="green")
            self.startBtn.config(state=tk.NORMAL)
        else:
            self.connectionStateText.config(text="Connection Not Established", foreground="black", background="gray")


        #configure thread control variable
        self.threadControllerGrahping = False
        self.threadControllerLabel = True
        self.isConnectionEstablished = False
        self.myThread2 = Thread(target = self.MyThread2, args = ())
        self.myThread2.start()

    def drop_down_callback(self, *args):
        print(self.displaySelection.get())
        if (self.graphingEnabled):
            f = Figure(figsize=(10, 4), dpi=100)
            self.a = f.add_subplot(111)
            if (self.displaySelection.get() == 'Atrium'):
                self.a.plot(range(len(self.setToGraph[0])), self.setToGraph[0])
            elif (self.displaySelection.get() == 'Ventrical'):
                self.a.plot(range(len(self.setToGraph[1])), self.setToGraph[1])
            elif (self.displaySelection.get() == 'Both'):
                self.a.plot(range(len(self.setToGraph[0])), self.setToGraph[0], self.setToGraph[1])
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=0, columnspan=3, padx=(135, 0), pady=(30, 0), sticky=tk.W)

    def load_current_user_json(self):
        return self.user_service.read(self.username).to_json()

    def toggleGraphing(self):
        if(self.threadControllerGrahping):
            self.threadControllerGrahping = False
            self.setToGraph = [[],[]]
        else:
            self.threadControllerGrahping = True
            myThread = Thread(target = self.MyThread, args = ())
            myThread.start()

        self.graphingEnabled = not (self.graphingEnabled)
        if (self.graphingEnabled):
            self.startBtn.config(text="Stop")
        else:
            self.startBtn.config(text="Start")
        if (self.graphingEnabled):
            f = Figure(figsize=(10, 4), dpi=100)
            self.a = f.add_subplot(111)
            if (self.displaySelection.get() == 'Atrium'):
                self.a.plot(range(len(self.setToGraph[0])), self.setToGraph[0])
            elif (self.displaySelection.get() == 'Ventrical'):
                self.a.plot(range(len(self.setToGraph[1])), self.setToGraph[1])
            elif (self.displaySelection.get() == 'Both'):
                self.a.plot(range(len(self.setToGraph[0])), self.setToGraph[0], self.setToGraph[1])
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=0, columnspan=3, padx=(135, 0), pady=(30, 0), sticky=tk.W)
        else:
            f = Figure(figsize=(10, 4), dpi=100)
            self.a = f.add_subplot(111)
            self.a.plot([0], [0])
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=0, columnspan=3, padx=(135, 0), pady=(30, 0), sticky=tk.W)

    def go_back(self):
        self.parent.switch_frame(MainPage.MainPage)
        self.threadControllerGrahping = False
        self.threadControllerLabel = False

    def MyThread2(self):
        ###This thread will disable the start button if there is no connection and if disconnection occurs while
        ### a device is connected it will act to end graphing then disable the button
        # start by trying to connect to the pacemaker
        if not self.serial_indicators.isConnected():
            self.serial_service.connect_to_pacemaker()
            if self.serial_service.is_connection_established():
                self.serial_indicators.setConnection(True)
                self.serial_indicators.setCurrConnectionID(self.serial_service.get_device_ID())
                self.serial_indicators.setLastConnectionID(self.serial_service.get_last_device_connected())

        while self.threadControllerLabel:
            if not self.threadControllerLabel:
                break
            time.sleep(1)
            if not self.threadControllerLabel:
                break
            if self.serial_indicators.isConnected():
                self.connectionStateText.config(text = "Connection Established", foreground="white", background = "green")
                self.startBtn.config(state=tk.NORMAL)
            else:
                self.connectionStateText.config(text = "Connection Not Established", foreground="black", background = "gray")

    def MyThread(self):
        #want to set thread controller based on if a device is connected
        while(self.threadControllerGrahping):
            print("Graphing...")
            if(not(self.threadControllerGrahping)):
                break
            time.sleep(0.1)
            if(not(self.threadControllerGrahping)):
                break
            self.addCntr = self.addCntr + 1
            self.setToGraph[0].append(math.sin(self.addCntr))
            self.setToGraph[1].append(self.addCntr**0.5)
            self.a.clear()
            f = Figure(figsize=(10, 4), dpi=100)
            self.a = f.add_subplot(111)
            if (self.displaySelection.get() == 'Atrium'):
                self.a.plot(range(len(self.setToGraph[0])), self.setToGraph[0])
            elif (self.displaySelection.get() == 'Ventrical'):
                self.a.plot(range(len(self.setToGraph[1])), self.setToGraph[1])
            elif (self.displaySelection.get() == 'Both'):
                self.a.plot(range(len(self.setToGraph[0])), self.setToGraph[0], self.setToGraph[1])
            #f.xlabel("Time", axes=self.a)
            #f.ylabel("Voltage (V)", axes=self.a)
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=0, columnspan=3, padx=(135, 0), pady=(30, 0), sticky=tk.W)
