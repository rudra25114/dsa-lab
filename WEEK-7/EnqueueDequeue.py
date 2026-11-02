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
        front = -1
        rear = -1
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
        return
    print("Circular Queue elements:")
    i = front
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % MAX
    print()

while True:
    print("\n--- CIRCULAR QUEUE ---")
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
