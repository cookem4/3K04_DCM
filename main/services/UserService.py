import json

from cryptography.fernet import InvalidToken

from main.data.pacingmode.PacingMode import PacingMode
from main.data.user.User import User, UserBuilder
from main.exceptions import MaxUsersExceededException
from main.repositories.JSONRepository import JSONRepository
from main.services.EncryptionService import EncryptionService
from main.services.Interfaces.CrudServiceInterface import CrudServiceInterface
from main.services.Interfaces.UserServiceInterface import UserServiceInterface


class UserService(UserServiceInterface, CrudServiceInterface):
    __user_file = "users.txt"
    __text_repo = JSONRepository(__user_file)
    __encryptor = EncryptionService()

    def __init__(self, testing_file=None):
        if testing_file is not None:
            self.user_file = testing_file
        else:
            self.user_file = "users.txt"
        self.__text_repo = JSONRepository(self.user_file)
        self.__encryptor = EncryptionService()

    ################################CRUD METHODS#############################################
    def create(self, user: User) -> None:
        if not self.exists(user.username):
            users_json = self.__text_repo.get()
            if len(users_json.keys()) >= 10:
                raise MaxUsersExceededException("Cannot hold more than 10 users, please remove a user to create a new "
                                                "one")
            else:
                users_json[user.username] = user.to_json()
                self.__save_user_json(users_json)

    def read(self, username: str) -> User:
        if self.exists(username):
            return UserBuilder().from_json(self.__text_repo.get()[username])

    def update(self, user: User) -> None:
        if self.exists(user.username):
            user_json = self.__text_repo.get()
            user_json[user.username] = user.to_json()
            self.__save_user_json(user_json)

    def delete(self, username: str) -> None:
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

    def exists(self, username) -> bool:
        # self.__print()
        try:
            return True if username in self.__text_repo.get() else False
        except InvalidToken:
            return False

    def verify(self, username, password) -> bool:
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
