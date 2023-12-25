# cloud_pos/domain/purchase.py
class Purchase:
    def __init__(self, purchase_id, products):
        self.purchase_id = purchase_id
        self.products = products
        self.total_cost = sum(product.price for product in products)

# Example usage:
# product1 = Product(product_id=1, name="Product1", price=10.0, stock_quantity=50)
# product2 = Product(product_id=2, name="Product2", price=20.0, stock_quantity=30)
# purchase = Purchase(purchase_id=1, products=[product1, product2])
