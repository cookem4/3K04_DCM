import tkinter as tk

import matplotlib

matplotlib.use("Agg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from main.views import MainPage
from main.views.AppFrameBase import AppFrameBase
from threading import Thread
import time
import math
import multiprocessing
import matplotlib.animation as animation
from main.data.egm import EGMPoint

class EGMDataPage(AppFrameBase):

    def __init__(self, parent):
        super().__init__(parent)

        self.username = self.session_service.get().username

        self.currUserJson = self.load_current_user_json()

        # The following are temporary values that are graphed when the drop down menu changes
        # Based on what drop down menu selection is chosen, this list will be indexed differently
        # This list will constantly be udpated from the serial module
        # First index is atrial pacing second is ventricle pacing
        # self.setToGraph = [[5, 6, 1, 3, 8, 9, 3, 5, 5, 6, 1, 3, 8, 9, 3, 5],
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 14, 15, 16]]
        self.setToGraph = [[0], [0], [0]]
        self.timeSum = 0
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

        # Setup labels based on pacing status
        if self.serial_indicators.isConnected():
            self.connectionStateText.config(text="Connection Established", foreground="white", background="green")
            self.startBtn.config(state=tk.NORMAL)
        else:
            self.connectionStateText.config(text="Connection Not Established", foreground="black", background="gray")

        myThread = Thread(target=self.ConnectionThread, args=())
        myThread.start()
        self.threadControllerLabel = True
        # Setup base graph
        global line, ax, canvas
        self.allowGraphing = False
        fig = matplotlib.figure.Figure(figsize=(10, 4), dpi=100)
        ax = fig.add_subplot(1, 1, 1)
        canvas = FigureCanvasTkAgg(fig, master=self)
        ax.set_xlabel("Time (ms)")
        ax.set_ylabel("Voltage")
        canvas.draw()
        canvas._tkcanvas.grid(row=3, column=0, columnspan=3, padx=(135, 0), pady=(30, 0), sticky=tk.W)
        line, = ax.plot([0], [0])
        ani = animation.FuncAnimation(fig, self.GraphAnimation, interval=200)
        canvas.draw()

    def GraphAnimation(self, i):
        if self.allowGraphing:
            ax.clear()
            if self.displaySelection.get() == 'Atrium':
                ax.plot(self.setToGraph[2], self.setToGraph[0])
                ax.set_ylim([min(self.setToGraph[0]) -1 , max(self.setToGraph[0]) + 1])
                ax.set_xlim([min(self.setToGraph[2]) - 5, max(self.setToGraph[1]) + 5])
            elif self.displaySelection.get() == 'Ventrical':
                ax.plot(self.setToGraph[2], self.setToGraph[1])
                ax.set_ylim([min(self.setToGraph[1])-1, max(self.setToGraph[1])+1])
                ax.set_xlim([min(self.setToGraph[2]) - 5, max(self.setToGraph[1]) + 5])
            elif self.displaySelection.get() == 'Both':
                ax.plot(self.setToGraph[2], self.setToGraph[0], self.setToGraph[1])
                ax.set_xlim([min(self.setToGraph[2]) - 5, max(self.setToGraph[1]) + 5])
                myMin = 0
                myMax = 0
                if(min(self.setToGraph[0]) > min(self.setToGraph[1])):
                    myMin = min(self.setToGraph[1])
                if(max(self.setToGraph[0]) > max(self.setToGraph[1])):
                    myMax = max(self.setToGraph[0])
                ax.set_ylim([myMin, myMax])
            ax.set_xlabel("Time (ms)")
            ax.set_ylabel("Voltage")


        else:
            ax.clear()

    def drop_down_callback(self, *args):
        print(self.displaySelection.get())

    def load_current_user_json(self):
        return self.user_service.read(self.username).to_json()

    def toggleGraphing(self):
        if self.allowGraphing:
            self.serial_service.end_egm_data()
            self.allowGraphing = False
            self.setToGraph = [[0], [0], [0]]
            self.timeSum = 0
        else:
            self.allowGraphing = True
            # Send request egm data command
            self.serial_service.request_EGM_data()
            myThread = Thread(target=self.FetchDataPoint, args=())
            myThread.start()

        if self.allowGraphing:
            self.startBtn.config(text="Stop")
        else:
            self.startBtn.config(text="Start")

    def go_back(self):
        self.allowGraphing = False
        self.threadControllerLabel = False
        self.parent.switch_frame(MainPage.MainPage)

    def ConnectionThread(self):
        ###This thread will disable the start button if there is no connection and if disconnection occurs while
        ### a device is connected it will act to end graphing then disable the button
        # start by trying to connect to the pacemaker
        if not self.serial_indicators.isConnected():
            self.serial_service.connect_to_pacemaker()
            if self.serial_service.is_connection_established():
                self.serial_indicators.setConnection(True)
                self.serial_indicators.setCurrConnectionID(self.serial_service.get_device_ID())
                self.serial_indicators.setLastConnectionID(self.serial_service.get_last_device_connected())

        if self.serial_indicators.isConnected():
            self.connectionStateText.config(text="Connection Established", foreground="white", background="green")
            self.startBtn.config(state=tk.NORMAL)
        else:
            self.connectionStateText.config(text="Connection Not Established", foreground="black", background="gray")
            self.startBtn.config(state=tk.DISABLED)
        i = 0
        lastDisconnectCheck = int(round(time.time() * 1000))
        while self.threadControllerLabel:
            time.sleep(0.5)
            if not self.allowGraphing:
                if int(round(time.time() * 1000)) - lastDisconnectCheck > 10000:
                    if self.serial_service.is_connection_established():
                        self.serial_indicators.setConnection(True)
                        self.serial_indicators.setCurrConnectionID(self.serial_service.get_device_ID())
                        self.serial_indicators.setLastConnectionID(self.serial_service.get_last_device_connected())
                        self.connectionStateText.config(text="Connection Established", foreground="white",
                                                        background="green")
                        self.startBtn.config(state=tk.NORMAL)
                    else:
                        self.serial_indicators.setConnection(False)
                        self.serial_indicators.setCurrConnectionID(None)
                        self.serial_indicators.setLastConnectionID(None)
                        self.startBtn.config(state=tk.DISABLED)
                        self.connectionStateText.config(text="Connection Not Established", foreground="black",
                                                        background="gray")
                    lastDisconnectCheck = int(round(time.time() * 1000))

    def FetchDataPoint(self):
        while self.allowGraphing:
            # Graph data point from serial module here:
            egmDataPoint = self.serial_service.get_graphing_data()
            if len(egmDataPoint) > len(self.setToGraph[0]):
                self.timeSum = self.timeSum + egmDataPoint[-1].period
                self.setToGraph[0].append(egmDataPoint[-1].atrium)
                self.setToGraph[1].append(egmDataPoint[-1].ventricle)
                self.setToGraph[2].append(self.timeSum)
            time.sleep(0.01)
