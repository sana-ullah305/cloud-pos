# cloud_pos/domain/transaction.py
class Transaction:
    def __init__(self, transaction_id):
        self.transaction_id = transaction_id
        self.products = []
        self.sale = None
        self.purchase = None

    def add_sale(self, sale):
        self.sale = sale

# Example usage:
# transaction = Transaction(transaction_id=1)
# sale = Sale(sale_id=1, products=[product1, product2])
# transaction.add_sale(sale)
