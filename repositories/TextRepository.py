import json

from services.EncryptionService import EncryptionService


class TextRepository:
    def __init__(self, filename):
        self.encryptor = EncryptionService()
        self.file = filename

    def get(self):
        with open(self.file, 'r') as file:
            s = file.read()
        return json.loads(self.encryptor.decrypt(s))

    def update(self, string: str):
        self.save(string)

    def save(self, string: str):
        with open(self.file, 'w') as file:
            file.write(self.encryptor.encrypt(string))
