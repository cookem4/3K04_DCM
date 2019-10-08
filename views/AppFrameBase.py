import tkinter as tk

from PIL import Image, ImageTk

from services.SessionService import SessionService


class AppFrameBase(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("DCM")
        self.configure(background="black")
        self.parent.configure(background="black")
        self.parent.geometry("1280x720")
        self.width = 600
        self.height = 300
        load = Image.open("views/assets/ecglineful.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=0, column=0, columnspan=1000, rowspan=1000, sticky=tk.N)

        self.session_service = SessionService.get_instance()
