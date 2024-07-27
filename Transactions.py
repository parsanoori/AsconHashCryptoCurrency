from typing import Dict, Any
from Transaction import Transaction
from ascon import hash


class Transactions:
    def __init__(self):
        self.mempool: Dict[str, Transaction] = {}

    def _getIndex(self, transaction: Transaction):
        data = transaction.data
        sender = transaction.from_account
        sgn = transaction.sign
        con = data + sender + sgn
        return hash(con.encode()).hex()

    def add(self, transaction: Transaction):
        if self.isIn(transaction):
            return
        index = self._getIndex(transaction)
        self.mempool[index] = transaction

    def remove(self, transaction: Transaction):
        index = self._getIndex(transaction)
        del self.mempool[index]

    def get(self, index: str) -> Transaction:
        return self.mempool[index]

    def isIn(self, transaction: Transaction):
        index = self._getIndex(transaction)
        return index in self.mempool

    def clear(self):
        self.mempool.clear()

    def size(self):
        return len(self.mempool)


