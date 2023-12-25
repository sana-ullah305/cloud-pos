class TransactionRepository:
    transactions = []

    @classmethod
    def save_transaction(cls, transaction):
        cls.transactions.append(transaction)

    @classmethod
    def get_transaction_by_id(cls, transaction_id):
        for transaction in cls.transactions:
            if transaction.transaction_id == transaction_id:
                return transaction
        return None
