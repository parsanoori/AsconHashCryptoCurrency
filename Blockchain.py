from Block import Block
from Transaction import Transaction
from Transactions import Transactions
from ascon import hash
from typing import Dict, Any
import ecdsa
import datetime
from configs import authority_pubkey, is_authority, authority_privkey
from ObjectExistsError import ObjectExistsError

class Blockchain:
    def generate_genesis_block(self) -> Block:
        data = "Genesis Block"
        prev_hash = "0"
        # sign using the authority private key
        sk = ecdsa.SigningKey.from_string(bytes.fromhex(authority_privkey), curve=ecdsa.SECP256k1)
        sign = sk.sign(hash(data.encode() + prev_hash.encode())).hex()
        return Block(data, prev_hash, sign)

    def __init__(self):
        genesis_block = self.generate_genesis_block()
        self.chain = [genesis_block]
        self.transactions = Transactions()
        self.head = genesis_block
        self.tail = genesis_block

    def add_block(self, block: Block):
        if block in self.chain:
            raise ObjectExistsError()
        if block.prev_hash != self.head.hash:
            raise ValueError("Block is not connected to the chain")
        self.chain.append(block)
        self.head = block

    def isCorrect(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].prev_hash != self.chain[i - 1].hash:
                return False
        return True

    def __iter__(self):
        return iter(self.chain)

    def __eq__(self, other):
        return self.chain == other.chain
