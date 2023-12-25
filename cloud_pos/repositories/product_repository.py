# cloud_pos/repositories/product_repository.py
class ProductRepository:
    products = []

    @classmethod
    def save_product(cls, product):
        cls.products.append(product)

    @classmethod
    def get_product_by_id(cls, product_id):
        for product in cls.products:
            if product.product_id == product_id:
                return product
        return None
