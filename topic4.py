from queue import Queue

class ECommercePlatform:
    def __init__(self, max_orders=100):
        self.order_queue = Queue(maxsize=max_orders)

    def place_order(self, order_details):
        
        if self.order_queue.full():
            print("Order queue is full. Cannot place new order.")
            return False
        else:
            self.order_queue.put(order_details)
            return True

    def process_next_order(self):
        
        if self.order_queue.empty():
            print("Order queue is empty.")
            return None
        else:
            order = self.order_queue.get()
            # Process the order (e.g., fulfill, ship)
            print(f"Processing order: {order}")
            return order

# Example usage
platform = ECommercePlatform()

# Place orders
order1 = {"customer_id": 1, "items": ["item1", "item2"]}
order2 = {"customer_id": 2, "items": ["item3"]}
order3 = {"customer_id": 3, "items": ["item4", "item5"]}

platform.place_order(order1)
platform.place_order(order2)
platform.place_order(order3)

# Process orders
processed_order1 = platform.process_next_order()
processed_order2 = platform.process_next_order()
print(f"Processed orders: {processed_order1}, {processed_order2}")
