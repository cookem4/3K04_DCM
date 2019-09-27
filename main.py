from services.UserService import UserService
from services.ConfigurationService import ConfigurationService
from data.PacingMode import PacingModes
from data.pacingmodes.AAI import AAI

if __name__ == '__main__':
    us = UserService()
    us.create("parker", "tits")
    cs = ConfigurationService()
    print(cs.get("parker", PacingModes.AAI).to_string())
    new_aai = AAI(1, 2, 3, 4)
    cs.update("parker", new_aai)
    print(cs.get("parker", PacingModes.AAI).to_string())
    us.delete("parker")
