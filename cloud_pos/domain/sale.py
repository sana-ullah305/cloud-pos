# cloud_pos/domain/sale.py
class Sale:
    def __init__(self, sale_id, products):
        self.sale_id = sale_id
        self.products = products
        self.total_amount = sum(product.price for product in products)

    def complete_sale(self):
        # Implement business logic for completing a sale
        for product in self.products:
            # Adjust stock quantities, assuming products are instances of Product class
            product.update_stock(-1)  # Decrease stock by 1 for each sold product
