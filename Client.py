from Transaction import Transaction
from requests import post
from ecdsa import SigningKey, VerifyingKey, SECP256k1

class Client:
    def __init__(self):
        self.sk = SigningKey.generate(curve=SECP256k1)
        self.vk = self.sk.get_verifying_key()
        self.account = self.vk.to_string().hex()

    def makeTxn(self, amount: int, to_account: str) -> Transaction:
        transaction = Transaction(f'{{"from": "{self.account}", "to": "{to_account}", "amount": {amount}}}', self.account)
        transaction.sign(self.sk.to_string().hex())
        return transaction

    def sendTxn(self, transaction: Transaction, server_ip: str, port: int):
        post(f'http://{server_ip}:{port}/transaction', json=transaction.dictData())


