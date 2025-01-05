class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_order(self, order):
        new_node = Node(order)
        new_node.next = self.head
        self.head = new_node

    def remove_order(self, order_id):
        temp = self.head
        prev = None

        while temp and temp.data['order_id'] != order_id:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Order not found.")
            return

        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next

    def display_orders(self):
    
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def add_order(self, priority, order):
        heapq.heappush(self.heap, (priority, order))

    def process_order(self):
        if not self.heap:
            print("No orders to process.")
            return None
        return heapq.heappop(self.heap)[1]

    def display_orders(self):
        for priority, order in self.heap:
            print(f"Priority: {priority}, Order: {order}")




# Managing orders using Singly Linked List
order_list = SinglyLinkedList()
order_list.add_order({'order_id': 1, 'customer': 'Alice', 'items': ['Apples', 'Bananas']})
order_list.add_order({'order_id': 2, 'customer': 'Bob', 'items': ['Oranges', 'Peaches']})
order_list.display_orders()
order_list.remove_order(1)
order_list.display_orders()

# Managing order priorities using Heap
order_heap = MinHeap()
order_heap.add_order(2, {'order_id': 3, 'customer': 'Charlie', 'items': ['Grapes', 'Mangoes']})
order_heap.add_order(1, {'order_id': 4, 'customer': 'Diana', 'items': ['Pineapples', 'Plums']})
order_heap.display_orders()
print("Processing order:", order_heap.process_order())
order_heap.display_orders()
