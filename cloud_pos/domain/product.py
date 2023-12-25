# cloud_pos/domain/product.py
class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        # Check if there is enough stock to update
        if self.stock_quantity + quantity >= 0:
            self.stock_quantity += quantity
            return True  # Stock updated successfully
        else:
            return False  # Insufficient stock

# Example usage:
# product = Product(product_id=1, name="Product1", price=10.0, stock_quantity=50)
# product.update_stock(-10)  # Decrease stock by 10
# product.update_stock(20)   # Increase stock by 20
