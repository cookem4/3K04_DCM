import abc


class EncryptionInterface(abc.ABC):

    @abc.abstractmethod
    def encrypt(self, message: str) -> str:  # takes in string and returns encrypted version
        pass

    @abc.abstractmethod
    def decrypt(self, message: str) -> str:  # takes encrypted string and returns original
        pass

    @abc.abstractmethod
    def hash(self, message: str) -> str:  # takes string and returns hash digest of string
        pass
