import abc

from main.data.Session import Session


class SessionInterface(abc.ABC):

    @abc.abstractmethod
    def get(self) -> Session:  # returns Session of currently logged in user
        pass

    @abc.abstractmethod
    def start_session(self, key: str) -> None:  # start a session using this key
        pass

    @abc.abstractmethod
    def validate(self, key: str) -> bool:  # returns boolean of whether a session is valid for given key
        pass

    @abc.abstractmethod
    def invalidate(self):  # invalidates current session
        pass
