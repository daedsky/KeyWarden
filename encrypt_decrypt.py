import base64
import json

import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class IncorrectPasswordError(Exception):
    pass

class EncrypterDecrypter:
    salt = b'\xaah\x84\xea#~s\xed\xe0\x9bAE#\xccb\xce'

    @staticmethod
    def write_json(fp, data):
        with open(fp, 'w') as f:
            j = json.dumps(data, indent=4)
            f.write(j)

    @staticmethod
    def read_json(fp):
        with open(fp, 'r') as f:
            j = json.load(f)
            return j

    @classmethod
    def create_master_pswd(cls, master_pswd):
        pswd = cls.encrypt(master_pswd, b"K3YW4RD3N@12345")
        data = {"token":pswd.decode()}
        cls.write_json('resources/data/master_pswd.json', data)

    @classmethod
    def convert_master_pswd_to_key(cls, master_pswd: bytes):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=32,
                         salt=cls.salt,
                         iterations=100000)

        key = base64.urlsafe_b64encode(kdf.derive(master_pswd))
        return key

    @classmethod
    def encrypt(cls, masterpswd: bytes, data: bytes):
        key = cls.convert_master_pswd_to_key(masterpswd)
        f = Fernet(key)
        token = f.encrypt(data)
        return token

    @classmethod
    def decrypt(cls, masterpswd: bytes, encrypted_data: bytes):
        try:
            key = cls.convert_master_pswd_to_key(masterpswd)
            f = Fernet(key)
            decrypted_data = f.decrypt(encrypted_data).decode()
            return decrypted_data
        except cryptography.fernet.InvalidToken:
            raise IncorrectPasswordError("Provided password is incorrect")


if __name__ == "__main__":
    print(EncrypterDecrypter.convert_master_pswd_to_key(b'L4vDE'))

