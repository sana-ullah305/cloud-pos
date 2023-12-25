class Transaction:
    def __init__(self, transaction_id):
        self.transaction_id = transaction_id
        self.products = []

    def add_product(self, product, quantity):
        # Business logic to add a product to the transaction
        pass

    def complete_transaction(self):
        # Business logic to complete the transaction
        pass
