import json
from json import JSONDecodeError

from cryptography.fernet import InvalidToken

from services.EncryptionService import EncryptionService
from repositories.interfaces.StringRepositoryInterface import StringRepositoryInterface


class JSONRepository(StringRepositoryInterface):
    __encryptor = EncryptionService()

    def __init__(self, filename):
        self.file = filename

    def get(self):
        with open(self.file, 'r') as file:
            s = file.read()
        try:
            return json.loads(self.__encryptor.decrypt(s))
        except (JSONDecodeError, InvalidToken) as e:
            print(e)
            return {}

    def save(self, json_string: str):
        with open(self.file, 'w') as file:
            file.write(self.__encryptor.encrypt(json_string))
