# This class is a Singleton, it will only ever have 1 active instantce
from data.Session import Session
from .Interfaces.SessionInterface import SessionInterface


class SessionService(SessionInterface):
    __instance = None
    __current_session: Session

    # invalidate tokens after 30 minutes

    @staticmethod
    def get_instance():
        """ Static Access Method """
        if SessionService.__instance == None:
            SessionService()
        return SessionService.__instance;

    def __init__(self):
        """ Virtually Private Constructor"""
        if SessionService.__instance != None:
            raise Exception("This class is a Singleton!")
        else:
            SessionService.__instance = self

    def get(self):
        if self.__current_session != None:
            return self.__current_session
        else:
            return None

    def start_session(self, username):
        self.__current_session = Session(username);

    def validate(self, username):
        return username == self.__current_session.username and self.__current_session.is_valid()

    def invalidate(self):
        self.__current_session = None
