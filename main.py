from cloud_pos.domain.store import Store
from cloud_pos.domain.terminal import Terminal
from cloud_pos.domain.product import Product
from cloud_pos.domain.transaction import Transaction
from cloud_pos.repositories.store_repository import StoreRepository
from cloud_pos.repositories.terminal_repository import TerminalRepository
from cloud_pos.repositories.transaction_repository import TransactionRepository

# Create a store
store = Store(store_id=1, name="MyStore")
StoreRepository.save_store(store)

# Add a terminal to the store
terminal = Terminal(terminal_id=1, location="Counter 1")
store.add_terminal(terminal)
TerminalRepository.save_terminal(terminal)

# Add products to the terminal
product1 = Product(product_id=1, name="Product1", price=10.0)
product2 = Product(product_id=2, name="Product2", price=20.0)

# Process a transaction
transaction = Transaction(transaction_id=1)
transaction.add_product(product1, quantity=2)
transaction.add_product(product2, quantity=1)
transaction.complete_transaction()

# Save the transaction
TransactionRepository.save_transaction(transaction)

# Retrieve and print the transaction
retrieved_transaction = TransactionRepository.get_transaction_by_id(transaction_id=1)

if retrieved_transaction:
    print("Transaction ID:", retrieved_transaction.transaction_id)
    print("Products:")
    for product, quantity in retrieved_transaction.products:
        print(f"- {product.name}: {quantity}")
else:
    print("Transaction not found.")
