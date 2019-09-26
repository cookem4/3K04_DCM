from data.Configuration import Configuration


class User:
    USERNAME = "username"
    PASSWORD = "password"
    CONFIG = "configurations"

    def __init__(self, username: str, password_hash: str, configurations: Configuration):
        self.username = username
        self.password_hash = password_hash
        self.configurations = configurations

    def to_json(self):
        return {User.USERNAME: self.username,
                User.PASSWORD: self.password_hash,
                User.CONFIG: self.configurations.to_string()}


class UserBuilder:
    def from_json(self, json_dict):
        return User(json_dict[User.USERNAME], json_dict[User.PASSWORD], json_dict[User.CONFIG])
