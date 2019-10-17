import abc


class StringRepositoryInterface(abc.ABC):

    @abc.abstractmethod
    def get(self):  # returns entire string stored in repo
        pass

    @abc.abstractmethod
    def save(self, string: str):  # replaces the entire repository with inputted string
        pass
