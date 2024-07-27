from fastapi import FastAPI
from Blockchain import Blockchain
from Transactions import Transactions
from Transaction import Transaction
from Block import Block
from configs import serve_port, serve_address, initially_known_nodes
import requests
from ObjectExistsError import ObjectExistsError
from threading import Thread
from pydantic import BaseModel
import uvicorn

class TransactionModel(BaseModel):
    data: str
    from_account: str
    sign: str


class BlockModel(BaseModel):
    data: str
    prev_hash: str
    sign: str


transactions = Transactions()
blockchain = Blockchain()
known_nodes = initially_known_nodes

app = FastAPI()


@app.post("/transaction")
def transaction(transaction: TransactionModel):
    transaction = Transaction(transaction.data, transaction.from_account, transaction.sign)
    try:
        transactions.add(transaction)
        # run propagate_transaction in a separate thread
        Thread(target=propagate_transaction, args=(transaction,)).start()
    except ObjectExistsError:
        return "Transaction already exists"
    return "Transaction added"


@app.post("/block")
def block(block: BlockModel):
    block = Block(block.data, block.prev_hash, block.sign)
    try:
        blockchain.add_block(block)
        # run propagate_block in a separate thread
        Thread(target=propagate_block, args=(block,)).start()
    except ObjectExistsError:
        return "Block already exists"
    return "Block added"


def propagate_block(block: Block):
    for node in known_nodes:
        requests.post(f'http://{node[0]}:{node[1]}/block', json=block)


def propagate_transaction(transaction: Transaction):
    for node in known_nodes:
        requests.post(f'http://{node[0]}:{node[1]}/transaction', json=transaction)


def main():
    uvicorn.run(app, host=serve_address, port=serve_port)
    while True:
        print("Enter a command: ")
        print("1. Add new node")
        print("2. Exit")
        command = input()
        if command == '1':
            print("Enter the IP address: ")
            ip = input()
            print("Enter the port: ")
            port = int(input())
            known_nodes.append((ip, port))
        elif command == '2':
            uvicorn.stop()
            break
        else:
            print("Invalid command")



if __name__ == '__main__':
    main()
