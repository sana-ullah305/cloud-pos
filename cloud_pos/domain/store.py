# cloud_pos/domain/store.py
class Store:
    def __init__(self, store_id, name):
        self.store_id = store_id
        self.name = name
        self.terminals = []
        self.products = []

    def add_product(self, product):
        # Business logic to add a product to the store
        pass
