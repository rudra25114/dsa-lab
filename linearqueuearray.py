MAX = 5
queue = []
front = 0
rear = -1

def enqueue():
    global rear
    if rear == MAX - 1:
        print("Queue Overflow")
    else:
        value = int(input("Enter element: "))
        queue.append(value)
        rear += 1
        print("Element inserted successfully")

def dequeue():
    global front
    if front > rear:
        print("Queue Underflow")
    else:
        print("Deleted element:", queue[front])
        front += 1

def peek():
    if front > rear:
        print("Queue is empty")
    else:
        print("Front element:", queue[front])

def display():
    if front > rear:
        print("Queue is empty")
    else:
        print("Queue elements:")
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()
