import json
from data.User import User
from data.User import UserBuilder
from data.Configuration import Configuration
from services.EncryptionService import EncryptionService
from data.PacingMode import PacingMode


class UserService:
    user_file = "../users.txt"

    def __init__(self):
        self.encryptor = EncryptionService()

    ################################CRUD METHODS#############################################

    def create(self, username, password):
        if not self.user_exists(username):
            users_json = self.__read_all()
            users_json[username] = User(username, self.encryptor.hash(password), Configuration()).to_json()
            self.__save_user_json(users_json)

    def read(self, username):
        if self.user_exists(username):
            return UserBuilder().from_json(self.__read_all()[username])

    def update(self, username, password, pacing_mode: PacingMode):
        if self.user_exists(username) and self.verify_user(username, password):
            user = self.read(username)
            user.configurations.set_pacing_mode(pacing_mode)
            user_json = self.__read_all()
            user_json[username] = user
            self.__save_user_json(user_json)

    def delete(self, username):
        if self.user_exists(username):
            user_json = self.__read_all()
            del user_json[username]
            self.__save_user_json(user_json)

    ####################################HELPER METHDOS#########################################

    def user_exists(self, username):
        return True if username in self.__read_all() else False

    def verify_user(self, username, password):
        if self.user_exists(username):
            user_json = self.__read_all()
            user = UserBuilder().from_json(user_json[username])
            return user.password_hash == self.encryptor.hash(password)
        return False

    ####################################PRIVATE METHODS##########################################

    def __read_all(self):
        with open(self.user_file, 'r') as file:
            s = file.read()
        return json.loads(self.encryptor.decrypt(s))

    def __save_user_json(self, users_json):
        users_str = json.dumps(users_json)
        with open(self.user_file, 'w') as file:
            file.write(self.encryptor.encrypt(users_str))

    def print(self):
        print(self.__read_all())


if __name__ == '__main__':
    us = UserService()
    us.create("parker", "tits")
    print(us.read("parker").configurations.aai)
    print(us.verify_user("parker", "tits"))
    us.delete("parker")
