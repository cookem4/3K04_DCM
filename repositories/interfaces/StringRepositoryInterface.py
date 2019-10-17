import abc


class StringRepositoryInterface(abc.ABC):

    @abc.abstractmethod
    def get(self) -> str:  # returns entire string stored in repo
        pass

    @abc.abstractmethod
    def save(self, string: str) -> None:  # replaces the entire repository with inputted string
        pass
