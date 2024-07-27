from ascon import hash
from configs import authority_pubkey
import ecdsa
import datetime


class Block:
    def __init__(self, data: str, prev_hash: str, sign: str):
        if data == "":
            raise ValueError("Block must have data")
        if prev_hash == "":
            raise ValueError("Block must have a previous hash")
        if sign == "":
            raise ValueError("Block must be signed")
        vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(authority_pubkey), curve=ecdsa.SECP256k1)
        h = hash(data.encode() + prev_hash.encode())
        if not vk.verify(bytes.fromhex(sign), h):
            raise ValueError("Block must be signed by the authority")
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = h.hex()
        self.sgn = sign

    def data(self):
        return self.data

    def sign(self):
        return self.sgn

    def __str__(self):
        return f'{self.data} {self.prev_hash} {self.sgn}'

    def __eq__(self, other):
        return self.data == other.data and self.prev_hash == other.prev_hash and self.sgn == other.sgn
