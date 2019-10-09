# This class is a Singleton, it will only ever have 1 active instantce
import datetime as dt


class Session:
    __timeout = dt.timedelta(minutes=30)

    def __init__(self, username):
        self.username = username
        self.datetime = dt.datetime.now();

    def is_valid(self):
        if dt.datetime.now() - self.datetime < self.__timeout:
            return True
        else:
            return False


class SessionService:
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

    def get_current_user(self):
        if self.__current_session != None:
            return self.__current_session.username
        else:
            return ""

    def start_session(self, username):
        self.__current_session = Session(username);

    def is_valid(self, username):
        return username == self.__current_session.username and self.__current_session.is_valid()

    def invalidate_session(self):
        self.__current_session = None
