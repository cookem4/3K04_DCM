from main.data.pacing.PacingMode import PacingMode
from main.data.pacing.PacingModeBuilder import PacingModeBuilder


class User:
    USERNAME = "username"
    PASSWORD = "password_hash"
    MODE = "pacing_mode_name"
    SETTINGS = "pacing_mode_settings"

    def __init__(self, username: str, password_hash: str, pacing_mode: PacingMode):
        self.username = username
        self.password_hash = password_hash
        self.pacing_mode = pacing_mode.NAME
        self.settings = pacing_mode

    def to_json(self):
        return {User.USERNAME: self.username,
                User.PASSWORD: self.password_hash,
                User.MODE: self.pacing_mode,
                User.SETTINGS: self.settings.to_string()}


class UserBuilder:
    @staticmethod
    def from_json(json_dict):
        return User(
            username=json_dict[User.USERNAME],
            password_hash=json_dict[User.PASSWORD],
            pacing_mode=PacingModeBuilder.from_string(json_dict[User.MODE], json_dict[User.SETTINGS])
        )

    @staticmethod
    def from_user_pass(username, password_hash):
        return User(
            username=username,
            password_hash=password_hash,
            pacing_mode=PacingModeBuilder().empty()
        )
