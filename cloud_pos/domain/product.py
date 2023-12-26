# cloud_pos/domain/product.py
class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock_quantity = stock_quantity

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock_quantity(self):
        return self._stock_quantity

    def increase_stock(self, quantity):
        """Increase the stock quantity."""
        self._stock_quantity += quantity

    def decrease_stock(self, quantity):
        """Decrease the stock quantity if there is sufficient stock."""
        if self.is_stock_sufficient:
            self._stock_quantity -= quantity

    @property
    def is_stock_sufficient(self):
        """Check if the stock is sufficient for a given operation."""
        return self._stock_quantity >= 0

    def __repr__(self):
        """String representation of the Product."""
        return f"Product(ID: {self._product_id}, Name: {self._name}, Price: {self._price}, Stock: {self._stock_quantity})"
