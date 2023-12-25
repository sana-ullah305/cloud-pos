# cloud_pos/services/store_service.py
from cloud_pos.domain.product import Product
from cloud_pos.domain.sale import Sale
from cloud_pos.domain.purchase import Purchase
from cloud_pos.domain.store import Store

class StoreService:
    @staticmethod
    def add_product(store, product_id, name, price, stock_quantity):
        product = Product(product_id=product_id, name=name, price=price, stock_quantity=stock_quantity)
        store.add_product(product)
        print(f"{name} added to the store with stock quantity {stock_quantity}.")

    @staticmethod
    def update_stock(store, product_id, new_stock_quantity):
        store.update_stock_in_store(product_id, new_stock_quantity)
        print(f"Stock quantity for product with ID {product_id} updated to {new_stock_quantity}.")

    @staticmethod
    def start_sale(store, sale_id):
        sale = Sale(sale_id=sale_id)
        while True:
            product_id = int(input("Enter product ID to add to sale (0 to finish): "))
            if product_id == 0:
                break
            product = next((p for p in store.products if p.product_id == product_id), None)
            if product:
                sale.add_product_to_sale(product)
                print(f"{product.name} added to the sale.")
            else:
                print("Product not found in the store.")
        sale.complete_sale()

    @staticmethod
    def start_purchase(store, purchase_id):
        purchase = Purchase(purchase_id=purchase_id)
        while True:
            product_id = int(input("Enter product ID to add to purchase (0 to finish): "))
            if product_id == 0:
                break
            product = next((p for p in store.products if p.product_id == product_id), None)
            if product:
                purchase.add_product_to_purchase(product)
                print(f"{product.name} added to the purchase.")
            else:
                print("Product not found in the store.")
        purchase.complete_purchase()

    @staticmethod
    def show_all_products(store):
        print("All Products:")
        for product in store.products:
            print(f"Product ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Stock: {product.stock_quantity}")
        print()

    @staticmethod
    def show_stock(store, product_id):
        product = next((p for p in store.products if p.product_id == product_id), None)
        if product:
            print(f"Stock for {product.name}: {product.stock_quantity}")
        else:
            print("Product not found in the store.")
        print()

    @staticmethod
    def show_products_on_sale(store):
        print("Products Currently on Sale:")
        on_sale_products = [product for product in store.products if product.price < product.original_price]
        for product in on_sale_products:
            print(f"Product ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Original Price: {product.original_price}")
        print()

    @staticmethod
    def show_products_in_purchase(store):
        print("Products Currently in Purchase:")
        in_purchase_products = [product for product in store.products if product.price > product.original_price]
        for product in in_purchase_products:
            print(f"Product ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Original Price: {product.original_price}")
        print()
