## Project Overview

This project implements a basic blockchain and transaction system using FastAPI for the API endpoints. The blockchain supports adding blocks and transactions, and propagates them to known nodes in the network.

## Features

- **Blockchain**: A simple blockchain implementation with genesis block creation, block addition, and chain validation.
- **Transactions**: Support for creating and adding transactions.
- **API Endpoints**: FastAPI endpoints for adding transactions and blocks.
- **Threaded Propagation**: Transactions and blocks are propagated to known nodes in separate threads.
- **Ascon Hashing**: Utilizes Ascon hash for lightweight and efficient hashing.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-repo/blockchain-project.git
    cd blockchain-project
    ```

2. **Create a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the FastAPI server**:
    ```sh
    python Node.py
    ```

2. **Interact with the API**:
    - **Add a transaction**:
        ```sh
        curl -X POST "http://localhost:8000/transaction" -H "Content-Type: application/json" -d '{"data": "some data", "from_account": "account1", "sign": "signature"}'
        ```
    - **Add a block**:
        ```sh
        curl -X POST "http://localhost:8000/block" -H "Content-Type: application/json" -d '{"data": "some data", "prev_hash": "previous hash", "sign": "signature"}'
        ```

## Project Structure

- `Node.py`: Main file to run the FastAPI server and handle API endpoints.
- `Blockchain.py`: Contains the `Blockchain` class and related methods.
- `Client.py`: Contains the `Client` class for creating and sending transactions.
- `Transaction.py`: Defines the `Transaction` class.
- `Block.py`: Defines the `Block` class.
- `configs.py`: Configuration file for server settings and initial known nodes.
- `requirements.txt`: List of dependencies.