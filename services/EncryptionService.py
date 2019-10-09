from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

import resources.resources as rs


class EncryptionService:
    def __init__(self):
        self.f = rs.fernet

    def encrypt(self, message):
        message = str.encode(message, 'ascii')
        return str(self.f.encrypt(message), 'utf-8')

    def decrypt(self, message):
        message = str.encode(message, 'ascii')
        return str(self.f.decrypt(message), "utf-8")

    def hash(self, message):
        message = str.encode(message, 'ascii')
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(message)
        return str(digest.finalize())
