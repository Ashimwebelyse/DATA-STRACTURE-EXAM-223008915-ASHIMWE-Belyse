
from collections import deque

class ECommercePlatform:
    def __init__(self):
        self.product_views = deque(maxlen=100)  # Track recent 100 product views
        self.cart_items = deque()  # Track cart items (can grow indefinitely)
        self.order_history = deque(maxlen=50)  # Track recent 50 orders

    def record_product_view(self, product_id):
        
        self.product_views.append(product_id)

    def get_recent_product_views(self):
        
        return list(self.product_views)

    def add_to_cart(self, product_id, quantity):
        
        self.cart_items.append((product_id, quantity))

    def remove_from_cart(self, product_id):
        
        for i, item in enumerate(self.cart_items):
            if item[0] == product_id:
                self.cart_items.pop(i)
                break

    def place_order(self, order_details):
        
        self.order_history.append(order_details)

    def get_order_history(self):
        
        return list(self.order_history)

# Example usage
platform = ECommercePlatform()

# Record product views
platform.record_product_view(1)
platform.record_product_view(2)
platform.record_product_view(3)
print("Recent product views:", platform.get_recent_product_views())

# Add items to cart
platform.add_to_cart(1, 2)
platform.add_to_cart(3, 1)
print("Cart items:", platform.cart_items)

# Place an order
order_details = {
    "customer_id": 123,
    "order_items": platform.cart_items,
    "total_amount": 150.00
}
platform.place_order(order_details)

# Get order history
print("Order history:", platform.get_order_history())