import json

from cryptography.fernet import InvalidToken
from .StringRepositoryInterface import StringRepositoryInterface
from services.EncryptionService import EncryptionService


class TextRepository(StringRepositoryInterface):
    def __init__(self, filename):
        self.encryptor = EncryptionService()
        self.file = filename

    def get(self):
        with open(self.file, 'r') as file:
            s = file.read()
        try:
            return json.loads(self.encryptor.decrypt(s))
        except InvalidToken:
            return {}

    def save(self, string: str):
        with open(self.file, 'w') as file:
            file.write(self.encryptor.encrypt(string))
