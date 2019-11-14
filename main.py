from main.views.GUIApplication import DCM_GUI
from main.communication.SerialCommunicator import test

if __name__ == '__main__':


    '''
    us = UserService()
    us.create("parker", "password")

    us.print()

    us.update_pacing_mode("parker", VVI(1, 2, 3, 4))

    us.print()
    us.delete("parker")
    '''
    
    # Create GUI instance
    app = DCM_GUI()
    app.mainloop()
    #test()
