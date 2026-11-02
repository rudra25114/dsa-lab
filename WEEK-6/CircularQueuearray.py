MAX = 5
queue = [None] * MAX
front = -1
rear = -1

def enqueue():
    global front, rear
    if (rear + 1) % MAX == front:
        print("Circular Queue Overflow")
        return

    value = int(input("Enter element: "))

    if front == -1:
        front = 0
        rear = 0
    else:
        rear = (rear + 1) % MAX

    queue[rear] = value
    print("Element inserted successfully")

def dequeue():
    global front, rear
    if front == -1:
        print("Circular Queue Underflow")
        return

    print("Deleted element:", queue[front])
    queue[front] = None

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % MAX

def peek():
    if front == -1:
        print("Queue is empty")
    else:
        print("Front element:", queue[front])

def display():
    if front == -1:
        print("Queue is empty")
    else:
        # Remaining code is not visible in the photo.
        pass
