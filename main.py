from services.UserService import UserService
from services.ConfigurationService import ConfigurationService
from data.PacingMode import PacingModes
from data.pacingmodes.AAI import AAI

if __name__ == '__main__':
    us = UserService()
    cs = ConfigurationService()

    us.create("parker", "stupid_password")
    print(cs.get("parker", PacingModes.AAI).to_string())
    cs.update("parker", AAI(1, 2, 3, 4))
    print(cs.get("parker", PacingModes.AAI).to_string())
    us.delete("parker")
