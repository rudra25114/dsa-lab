class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node
        print("Linked List created successfully")

    # 2. Insert at Beginning
    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    # 3. Insert at End
    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at the end.")
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data} at the end.")

    # 4. Insert at Index
    def insert_at_index(self):
        data = int(input("Enter data: "))
        index = int(input("Enter index: "))

        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted {data} at index {index}.")
            return

        temp = self.head
        for i in range(index - 1):
            if temp is None:
                print("Index out of range")
                return
            temp = temp.next

        if temp is None:
            print("Index out of range")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        print(f"Inserted {data} at index {index}.")

    # 5. Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        self.head = self.head.next
        print(f"Deleted {temp.data} from beginning.")

    # 6. Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            print(f"Deleted {self.head.data} from end.")
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        print(f"Deleted {temp.next.data} from end.")
        temp.next = None

    # 7. Delete at Index
    def delete_at_index(self):
        if self.head is None:
            print("List is empty")
            return
        index = int(input("Enter index: "))
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            print(f"Deleted {self.head.data} from index 0.")
            self.head = self.head.next
            return

        temp = self.head
        for i in range(index - 1):
            if temp is None or temp.next is None:
                print("Index out of range")
                return
            temp = temp.next

        if temp.next is None:
            print("Index out of range")
            return

        print(f"Deleted {temp.next.data} from index {index}.")
        temp.next = temp.next.next

    # 8. Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        print("Linked List: ", end="")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 9. Count Nodes
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        print(f"Total nodes: {count}")

    # 10. Search
    def search(self):
        data = int(input("Enter data to search: "))
        temp = self.head
        index = 0
        while temp is not None:
            if temp.data == data:
                print(f"Element found at index {index}")
                return
            temp = temp.next
            index += 1
        print("Element not found")


# Main Program
sll = SLL()

while True:
    print("\n----- SINGLY LINKED LIST -----")
    print("1. Create Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Index")
    print("5. Delete from Beginning")
    print("6. Delete from End")
    print("7. Delete from Index")
    print("8. Display")
    print("9. Count Nodes")
    print("10. Search")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sll.create()
    elif choice == 2:
        sll.insert_beginning()
    elif choice == 3:
        sll.insert_end()
    elif choice == 4:
        sll.insert_at_index()
    elif choice == 5:
        sll.delete_beginning()
    elif choice == 6:
        sll.delete_end()
    elif choice == 7:
        sll.delete_at_index()
    elif choice == 8:
        sll.display()
    elif choice == 9:
        sll.count_nodes()
    elif choice == 10:
        sll.search()
    elif choice == 11:
        print("Exiting from the program...")
        break
    else:
        print("Invalid choice")
