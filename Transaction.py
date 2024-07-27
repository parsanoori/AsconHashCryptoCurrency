import ecdsa
from ascon import hash
import json


class Transaction:
    def __init__(self, data: str, from_account: str, sign: str = ""):
        self.data = data
        self.dictData = json.loads(data)
        self.sgn = sign
        self.from_account = from_account

    def dictData(self):
        # convert the self.data to a dictionary
        return self.dictData

    def sign(self, private_key: str):
        sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
        self.sgn = sk.sign(hash(self.data.encode())).hex()

    def verify(self):
        vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(self.from_account), curve=ecdsa.SECP256k1)
        return vk.verify(bytes.fromhex(self.sgn), hash(self.data.encode()))

    def __str__(self):
        return f'{self.data} {self.from_account}'
