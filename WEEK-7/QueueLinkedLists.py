class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

front = None
rear = None

def enqueue():
    global front, rear
    value = int(input("Enter element: "))
    new_node = Node(value)
    if rear is None:
        front = rear = new_node
    else:
        rear.next = new_node
        rear = new_node
    print("Element inserted successfully")

def dequeue():
    global front, rear
    if front is None:
        print("Queue Underflow")
    else:
        print("Deleted element:", front.data)
        front = front.next
        if front is None:
            rear = None

def peek():
    if front is None:
        print("Queue is empty")
    else:
        print("Front element:", front.data)

def display():
    if front is None:
        print("Queue is empty")
    else:
        temp = front
        print("Queue elements:")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

while True:
    print("\n--- QUEUE USING LINKED LIST ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
