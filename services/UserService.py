import json

from cryptography.fernet import InvalidToken

from data.PacingMode import PacingMode
from data.User import User, UserBuilder
from repositories.TextRepository import TextRepository
from services.EncryptionService import EncryptionService
from services.Interfaces.CrudServiceInterface import CrudServiceInterface
from services.Interfaces.UserServiceInterface import UserServiceInterface
from exceptions.MaxUsersExceededException import MaxUsersExceededException


class UserService(UserServiceInterface, CrudServiceInterface):
    __user_file = "users.txt"
    __text_repo = TextRepository(__user_file)
    __encryptor = EncryptionService()

    ################################CRUD METHODS#############################################
    def create(self, user: User):
        if not self.exists(user.username):
            users_json = self.__text_repo.get()
            if len(users_json.keys()) >= 10:
                raise MaxUsersExceededException("Cannot hold more than 10 users, please remove a user to create a new "
                                                "one")
            else:
                users_json[user.username] = user.to_json()
                self.__save_user_json(users_json)

    def read(self, username: str):
        if self.exists(username):
            return UserBuilder().from_json(self.__text_repo.get()[username])

    def update(self, user: User):
        if self.exists(user.username):
            user_json = self.__text_repo.get()
            user_json[user.username] = user.to_json()
            self.__save_user_json(user_json)

    def delete(self, username: str):
        if self.exists(username):
            user_json = self.__text_repo.get()
            del user_json[username]
            self.__save_user_json(user_json)

    ####################################HELPER METHDOS#########################################

    def create_by_username_and_password(self, username, password):
        self.create(UserBuilder.from_user_pass(username, self.__encryptor.hash(password)))

    def update_pacing_mode(self, username, pacing_mode: PacingMode):
        if self.exists(username):
            user = self.read(username)
            user.pacing_mode = pacing_mode.NAME
            user.settings = pacing_mode
            self.update(user)

    def exists(self, username):
        self.__print()
        try:
            return True if username in self.__text_repo.get() else False
        except InvalidToken:
            return False

    def verify(self, username, password):
        if self.exists(username):
            user_json = self.__text_repo.get()
            user = UserBuilder().from_json(user_json[username])
            return user.password_hash == self.__encryptor.hash(password)
        return False

    ####################################PRIVATE METHODS##########################################
    def __save_user_json(self, users_json):
        users_str = json.dumps(users_json)
        self.__text_repo.save(users_str)

    def __print(self):
        print(self.__text_repo.get())
