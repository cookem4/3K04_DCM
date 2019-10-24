import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

keypass: bytes = b"p@c3m@k3r"
salt: bytes = b"12345"

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA3_256(),
    length=32,
    salt=salt,
    iterations=10000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(keypass))
fernet = Fernet(key)
