from services.UserService import UserService
from views.GUIApplication import DCM_GUI

if __name__ == '__main__':
    us = UserService()
    us.create("parker", "password")

    # Create GUI instance
    app = DCM_GUI()
    app.mainloop()

    # print(cs.get("parker", PacingModes.AAI).to_string())
    # cs.update("parker", AAI(1, 2, 3, 4))
    # print(cs.get("parker", PacingModes.AAI).to_string())
    # us.delete("parker")
