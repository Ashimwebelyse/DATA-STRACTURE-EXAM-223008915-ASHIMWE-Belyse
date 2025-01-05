class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("The given previous node must be in LinkedList")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage in an e-commerce platform
class Order:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items

# Create an order processing system using a linked list
order_processing_system = LinkedList()

# Place orders
order1 = Order(1, "Alice", ["item1", "item2"])
order2 = Order(2, "Bob", ["item3"])
order3 = Order(3, "Charlie", ["item4", "item5"])

order_processing_system.append(order1)
order_processing_system.append(order2)
order_processing_system.prepend(order3)

# Process orders (example: simulate processing by printing order details)
print("Processing orders:")
current_order = order_processing_system.head
while current_order:
    print(f"Order ID: {current_order.data.order_id}, Customer: {current_order.data.customer_name}")
    current_order = current_order.next