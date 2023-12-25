# cloud_pos/domain/transaction.py
class Transaction:
    def __init__(self, transaction_id):
        self.transaction_id = transaction_id
        self.products = []
        self.sale = None
        self.purchase = None

    def add_sale(self, sale):
        # Business logic to associate a sale with the transaction
        pass

    def add_purchase(self, purchase):
        # Business logic to associate a purchase with the transaction
        pass
