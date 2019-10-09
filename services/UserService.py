import json

from cryptography.fernet import InvalidToken

from data.PacingMode import PacingMode
from data.PacingModeBuilder import PacingModeBuilder
from data.User import User, UserBuilder
from repositories.TextRepository import TextRepository
from services.EncryptionService import EncryptionService


class UserService:
    user_file = "users.txt"

    def __init__(self):
        self.text_repo = TextRepository(self.user_file)
        self.encryptor = EncryptionService()

    ################################CRUD METHODS#############################################
    def create(self, username, password):
        if not self.user_exists(username):
            users_json = self.text_repo.get()
            if len(users_json.keys()) >= 10:
                raise Exception("Cannot hold more than 10 users, please remove a user to create a new one")
            else:
                users_json[username] = User(username, self.encryptor.hash(password), PacingModeBuilder.empty()).to_json()
                self.__save_user_json(users_json)

    def read(self, username):
        if self.user_exists(username):
            return UserBuilder().from_json(self.text_repo.get()[username])

    def update(self, user: User):
        if self.user_exists(user.username):
            user_json = self.text_repo.get()
            user_json[user.username] = user.to_json()
            self.__save_user_json(user_json)

    def update_pacing_mode(self, username, pacing_mode: PacingMode):
        if self.user_exists(username):
            user = self.read(username)
            user.pacing_mode = pacing_mode.NAME
            user.settings = pacing_mode
            self.update(user)

    def delete(self, username):
        if self.user_exists(username):
            user_json = self.text_repo.get()
            del user_json[username]
            self.__save_user_json(user_json)

    ####################################HELPER METHDOS#########################################

    def user_exists(self, username):
        try:
            return True if username in self.text_repo.get() else False
        except InvalidToken:
            return False

    def verify_user(self, username, password):
        if self.user_exists(username):
            user_json = self.text_repo.get()
            user = UserBuilder().from_json(user_json[username])
            return user.password_hash == self.encryptor.hash(password)
        return False

    def print(self):
        print(json.dumps(self.text_repo.get(), indent=4, sort_keys=True))

    def getJSON(self):
        return json.dumps(self.text_repo.get(), indent=4, sort_keys=True)

    ####################################PRIVATE METHODS##########################################
    def __save_user_json(self, users_json):
        users_str = json.dumps(users_json)
        self.text_repo.save(users_str)
