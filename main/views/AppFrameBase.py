import tkinter as tk

from PIL import Image, ImageTk

from main.services.SessionService import SessionService
from main.services.UserService import UserService
from main.communication.SerialCommunicator import SerialCommunicator

class AppFrameBase(tk.Frame):
    session_service: SessionService = SessionService.get_instance()
    user_service: UserService = UserService()

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("DCM")
        self.configure(background="black")
        self.parent.configure(background="black")
        self.parent.geometry("1280x720")
        self.width = 600
        self.height = 300
        load = Image.open("main/views/assets/ecglineful.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=0, column=0, columnspan=1000, rowspan=1000, sticky=tk.N)
