import abc

from data.PacingMode import PacingMode
from .CrudServiceInterface import CrudServiceInterface


class UserServiceInterface(CrudServiceInterface):

    @abc.abstractmethod
    def create_by_username_and_password(self, username: str, password: str) -> None:
        # creates and saves new user by username and password
        pass

    @abc.abstractmethod
    def update_pacing_mode(self, username: str, pacing_mode: PacingMode) -> None:
        # updates pacing mode for given username
        pass

    @abc.abstractmethod
    def exists(self, username: str) -> bool:
        # returns True if username exists in repository
        pass

    @abc.abstractmethod
    def verify(self, username, password) -> bool:
        # returns true is username password combination exists in repository
        pass
