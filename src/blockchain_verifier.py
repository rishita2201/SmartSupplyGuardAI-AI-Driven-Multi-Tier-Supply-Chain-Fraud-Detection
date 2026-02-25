import hashlib

class BlockchainVerifier:
    def __init__(self):
        self.chain = []

    def add_transaction(self, transaction):
        tx_hash = hashlib.sha256(str(transaction).encode()).hexdigest()
        self.chain.append({
            'transaction': transaction,
            'hash': tx_hash
        })
        return tx_hash

    def verify_transaction(self, transaction):
        tx_hash = hashlib.sha256(str(transaction).encode()).hexdigest()
        for block in self.chain:
            if block['hash'] == tx_hash:
                return True
        return False
