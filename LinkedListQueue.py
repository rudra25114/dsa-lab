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

    if front is None:
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
