from src.store.customerstore import CustomerStore
from src.view.customerview import CustomerView


def check():
    """
    Entry point:
    - Creates 100 customers
    - Displays customer details
    """
    customer_store = CustomerStore(num_customers=100)
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()


if __name__ == "__main__":
    check()