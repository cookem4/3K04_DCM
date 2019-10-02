import tkinter as tk
from PIL import Image, ImageTk

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
        load = Image.open("ecglineful.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=0, column=0, columnspan=1000, rowspan=1000, sticky=tk.N)
        
