from main.views.GUIApplication import DCM_GUI
from test.communication.MockPacemaker import MockPacemaker

if __name__ == '__main__':

    '''
    us = UserService()
    us.create("parker", "password")

    us.print()

    us.update_pacing_mode("parker", VVI(1, 2, 3, 4))

    us.print()
    us.delete("parker")
    '''
    # serialTest = SerialCommunicator("COM12")
    # print(serialTest.is_connection_established())
    # Create GUI instance
    app = DCM_GUI()
    app.mainloop()
