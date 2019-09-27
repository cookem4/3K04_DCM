from data.PacingMode import PacingMode
from data.PacingMode import PacingModes

from services.UserService import UserService


class ConfigurationService:

    def __init__(self):
        self.user_service = UserService()

    def update(self, username, pacing_mode: PacingMode):
        if self.user_service.user_exists(username):
            user = self.user_service.read(username)
            user.configurations.set_pacing_mode(pacing_mode)
            self.user_service.update(user)

    def get(self, username, pacingmode: PacingModes):
        return self.user_service.read(username).configurations.get(pacingmode)
