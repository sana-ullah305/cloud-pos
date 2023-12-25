# cloud_pos/domain/sale.py
class Sale:
    def __init__(self, sale_id, products):
        self.sale_id = sale_id
        self.products = products
        self.total_amount = sum(product.price for product in products)

# Example usage:
# product1 = Product(product_id=1, name="Product1", price=10.0, stock_quantity=50)
# product2 = Product(product_id=2, name="Product2", price=20.0, stock_quantity=30)
# sale = Sale(sale_id=1, products=[product1, product2])
