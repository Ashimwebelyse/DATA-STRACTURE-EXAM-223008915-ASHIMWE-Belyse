def heapify(arr, n, i):

    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than the root
    if left < n and arr[left]['priority'] > arr[largest]['priority']:
        largest = left

    # Check if right child exists and is greater than the current largest
    if right < n and arr[right]['priority'] > arr[largest]['priority']:
        largest = right

    # Swap and continue heapifying if root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)


# Example Usage
if __name__ == "__main__":
    # Example data: Orders with priorities
    orders = [
        {"order_id": 101, "customer": "Alice", "priority": 3},
        {"order_id": 102, "customer": "Bob", "priority": 5},
        {"order_id": 103, "customer": "Charlie", "priority": 1},
        {"order_id": 104, "customer": "Diana", "priority": 4},
        {"order_id": 105, "customer": "Eve", "priority": 2},
    ]

    print("Before sorting:")
    for order in orders:
        print(order)

    # Sort orders based on priority
    heap_sort(orders)

    print("\nAfter sorting (by descending priority):")
    for order in orders:
        print(order)
