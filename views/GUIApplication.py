import tkinter as tk
from views.LoginPage import LoginPage


class DCM_GUI(tk.Tk):
    def __init__(self):
        # initializes the main window
        tk.Tk.__init__(self)
        self._frame = None
        # Goes to the first screen
        self.switch_frame(LoginPage)

    # As the name says, a frame name is passed in and the window switches its displayed frame
    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()


if __name__ == "__main__":
    app = DCM_GUI()
    app.mainloop()
