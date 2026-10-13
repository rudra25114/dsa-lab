# Node class for Circular Queue Linked List implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 1. Circular Queue using Linked List
class CircularQueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def nQ(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self.rear.next = self.front  # Point to itself to make it circular
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Maintain circular link
        print(f"Enqueued (LL): {item}")

    def dQ(self):
        if self.is_empty():
            print("Queue Underflow! Circular Queue is empty.")
            return None
        
        dequeued_item = self.front.data
        
        # If there is only one element in the queue
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front  # Maintain circular link
            
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
        
        print("Circular Queue (Linked List) [Front -> Rear]: ", end="")
        temp = self.front
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.front:
                break
        print("(Back to Front: " + str(self.front.data) + ")")


# 2. Circular Queue using Array (Fixed-size list)
class CircularQueueArray:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def nQ(self, item):
        if self.is_full():
            print("Queue Overflow! Circular Queue is full.")
            return
        
        if self.front == -1:  # First element insertion
            self.front = 0
            
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Enqueued (Array): {item}")

    def dQ(self):
        if self.is_empty():
            print("Queue Underflow! Circular Queue is empty.")
            return None
        
        dequeued_item = self.queue[self.front]
        self.queue[self.front] = None  # Clear memory slot visually
        
        if self.front == self.rear:  # Element was the last remaining item
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
            
        print(f"Dequeued (Array): {dequeued_item}")
        return dequeued_item

    def peak(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        
        print("Raw Array State:", self.queue)
        print("Circular Queue (Array elements from Front to Rear): ", end="")
        
        temp = self.front
        while True:
            print(self.queue[temp], end=" ")
            if temp == self.rear:
                break
            temp = (temp + 1) % self.size
        print()


# Menu-driven runner function
def main():
    print("Select Circular Queue Implementation:")
    print("1. Array (Fixed-size Python List)")
    print("2. Linked List")
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == '1':
        try:
            size = int(input("Enter the fixed capacity of the circular array: "))
            if size <= 0:
                raise ValueError
        except ValueError:
            print("Invalid size! Defaulting size to 5.")
            size = 5
        q = CircularQueueArray(size)
        name = "Array"
    elif choice == '2':
        q = CircularQueueLinkedList()
        name = "Linked List"
    else:
        print("Invalid choice. Exiting.")
        return

    while True:
        print(f"\n--- Circular Queue Menu ({name} Implementation) ---")
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
            print("Invalid option! Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
