# cloud_pos/domain/store.py
class Store:
    def __init__(self, store_id, name):
        self.store_id = store_id
        self.name = name
        self.terminals = []
        self.products = []

    def add_product(self, product):
        existing_product = next((p for p in self.products if p.product_id == product.product_id), None)
        if existing_product:
            existing_product.update_stock(product.stock_quantity)
        else:
            self.products.append(product)

# Example usage:
# store = Store(store_id=1, name="MyStore")
# product = Product(product_id=1, name="Product1", price=10.0, stock_quantity=50)
# store.add_product(product)