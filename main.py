from cloud_pos.domain.store import Store
from cloud_pos.domain.terminal import Terminal
from cloud_pos.domain.product import Product
from cloud_pos.domain.purchase import Purchase
from cloud_pos.domain.sale import Sale
from cloud_pos.domain.transaction import Transaction
from cloud_pos.repositories.store_repository import StoreRepository
from cloud_pos.repositories.terminal_repository import TerminalRepository
from cloud_pos.repositories.transaction_repository import TransactionRepository
from cloud_pos.services.store_service import StoreService

def main():
    store = Store(store_id=1, name="MyStore")
    store_service = StoreService()

    while True:
        print("1. Add product to store")
        print("2. Update stock quantity for a product in the store")
        print("3. Start a sale")
        print("4. Start a purchase")
        print("5. Show all products")
        print("6. Show stock for a specific product")
        print("7. Show products currently on sale")
        print("8. Show products currently in purchase")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            store_service.add_product(store, product_id=1, name="Product1", price=10.0, stock_quantity=50)
        elif choice == "2":
            store_service.update_stock(store, product_id=1, new_stock_quantity=100)
        elif choice == "3":
            store_service.start_sale(store, sale_id=1)
        elif choice == "4":
            store_service.start_purchase(store, purchase_id=1)
        elif choice == "5":
            store_service.show_all_products(store)
        elif choice == "6":
            store_service.show_stock(store, product_id=1)
        elif choice == "7":
            store_service.show_products_on_sale(store)
        elif choice == "8":
            store_service.show_products_in_purchase(store)
        elif choice == "9":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()