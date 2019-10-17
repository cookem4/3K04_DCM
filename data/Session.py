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
