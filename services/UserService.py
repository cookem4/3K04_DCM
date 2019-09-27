import json

from data.Configuration import Configuration
from data.User import User
from data.User import UserBuilder
from repositories.TextRepository import TextRepository
from services.EncryptionService import EncryptionService


class UserService:
    user_file = "users.txt"

    def __init__(self):
        self.text_repo = TextRepository(self.user_file)
        self.encryptor = EncryptionService()

    ################################CRUD METHODS#############################################
    def create(self, username, password, configuration=Configuration()):
        if not self.user_exists(username):
            users_json = self.text_repo.get()
            users_json[username] = User(username, self.encryptor.hash(password), configuration).to_json()
            self.__save_user_json(users_json)

    def read(self, username):
        if self.user_exists(username):
            return UserBuilder().from_json(self.text_repo.get()[username])

    def update(self, user: User):
        if self.user_exists(user.username):
            user_json = self.text_repo.get()
            user_json[user.username] = user.to_json()
            self.__save_user_json(user_json)

    def delete(self, username):
        if self.user_exists(username):
            user_json = self.text_repo.get()
            del user_json[username]
            self.__save_user_json(user_json)

    ####################################HELPER METHDOS#########################################

    def user_exists(self, username):
        return True if username in self.text_repo.get() else False

    def verify_user(self, username, password):
        if self.user_exists(username):
            user_json = self.text_repo.get()
            user = UserBuilder().from_json(user_json[username])
            return user.password_hash == self.encryptor.hash(password)
        return False

    ####################################PRIVATE METHODS##########################################
    def __save_user_json(self, users_json):
        users_str = json.dumps(users_json)
        self.text_repo.save(users_str)
