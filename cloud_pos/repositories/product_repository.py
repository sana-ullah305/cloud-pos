# cloud_pos/repositories/product_repository.py
from cloud_pos.domain.product import Product

class ProductRepository:
    def __init__(self):
        """Initialize the ProductRepository."""
        # Using a dictionary to simulate an in-memory data storage
        self.products = {}

    def add_product(self, product):
        """Add a product to the repository.

        Args:
            product (Product): The product object to be added.
        """
        self.products[product.product_id] = product

    def update_product(self, product_id, new_product_data):
        """Update product information in the repository.

        Args:
            product_id (int): The ID of the product to be updated.
            new_product_data (dict): A dictionary containing new data for the product.
        """
        product = self.products.get(product_id)
        if product:
            product._name = new_product_data.get('name', product._name)
            product._price = new_product_data.get('price', product._price)
            product.increase_stock(new_product_data.get('stock_quantity', 0))

    def get_product_by_id(self, product_id):
        """Retrieve a product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product: The product object if found, otherwise None.
        """
        return self.products.get(product_id)

    def get_all_products(self):
        """Retrieve all products in the repository.

        Returns:
            list: A list containing all product objects.
        """
        return list(self.products.values())

    def delete_product(self, product_id):
        """Delete a product from the repository.

        Args:
            product_id (int): The ID of the product to be deleted.
        """
        if product_id in self.products:
            del self.products[product_id]
