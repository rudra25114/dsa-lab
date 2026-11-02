# Node class for Linked List implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue using Linked List
class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def nQ(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued (LL): {item}")

    def dQ(self):
        if self.is_empty():
            print("Queue Underflow! Queue is empty.")
            return None
        dequeued_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued (LL): {dequeued_item}")
        return dequeued_item

    def peak(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        temp = self.front
        print("Queue (Linked List) [Front -> Rear]: ", end="")
        while temp:
            print(temp.data, end=" <- ")
            temp = temp.next
        print("None")

# Queue using Array (Python List)
class QueueArray:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def nQ(self, item):
        self.queue.append(item)
        print(f"Enqueued (Array): {item}")

    def dQ(self):
        if self.is_empty():
            print("Queue Underflow! Queue is empty.")
            return None
        dequeued_item = self.queue.pop(0)
        print(f"Dequeued (Array): {dequeued_item}")
        return dequeued_item

    def peak(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[0]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue (Array) [Front -> Rear]:", self.queue)

# Menu-driven runner function
def main():
    print("Select Queue Implementation:")
    print("1. Array (Python List)")
    print("2. Linked List")
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == '1':
        q = QueueArray()
        name = "Array"
    elif choice == '2':
        q = QueueLinkedList()
        name = "Linked List"
    else:
        print("Invalid choice. Exiting.")
        return

    while True:
        print(f"\n--- Queue Menu ({name} Implementation) ---")
        print("1. nQ (Enqueue)")
        print("2. dQ (Dequeue)")
        print("3. Peak")
        print("4. Display")
        print("5. Exit")
        
        opt = input("Enter your option (1-5): ").strip()
        
        if opt == '1':
            val = input("Enter value to enqueue: ")
            q.nQ(val)
        elif opt == '2':
            q.dQ()
        elif opt == '3':
            front_val = q.peak()
            if front_val is not None:
                print(f"Peak element (Front): {front_val}")
        elif opt == '4':
            q.display()
        elif opt == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option! Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
