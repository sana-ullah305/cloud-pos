# cloud_pos/domain/purchase.py
class Purchase:
    def __init__(self, purchase_id):
        self.purchase_id = purchase_id
        self.products = []
        self.total_cost = 0

    def add_product_to_purchase(self, product):
        self.products.append(product)
        self.total_cost += product.price

    def complete_purchase(self):
        print("Purchase completed!")
        for product in self.products:
            product.update_stock(1)
        print("Stock updated.")
