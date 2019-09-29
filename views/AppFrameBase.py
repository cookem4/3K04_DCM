import tkinter as tk


class AppFrameBase(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("DCM")
        self.configure(background="black")
        self.parent.configure(background="black")
        self.parent.geometry("1280x720")
        self.width = 1280
        self.height = 720
