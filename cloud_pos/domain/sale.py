# cloud_pos/domain/sale.py
class Sale:
    def __init__(self, sale_id):
        self.sale_id = sale_id
        self.products = []
        self.total_amount = 0

    def add_product_to_sale(self, product):
        self.products.append(product)
        self.total_amount += product.price

    def complete_sale(self):
        print("Sale completed!")
        for product in self.products:
            product.update_stock(-1)
        print("Stock updated.")