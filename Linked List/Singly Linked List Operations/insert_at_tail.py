class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, val):
        new_node = Node(val)

        # List is empty
        if self.head is None:
            self.head = new_node
            return

        # Go to last node
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next

        # Connect new node
        tmp.next = new_node

    def print_linked_list(self):
        print("Your Linked List:", end=" ")

        tmp = self.head
        while tmp is not None:
            print(tmp.val, end=" ")
            tmp = tmp.next

        print()


ll = LinkedList()

while True:
    print("\nOption 1: Insert at Tail")
    print("Option 2: Print Linked List")
    print("Option 3: Exit")

    op = int(input("Enter option: "))

    if op == 1:
        value = int(input("Enter value: "))
        ll.insert_at_tail(value)

    elif op == 2:
        ll.print_linked_list()

    elif op == 3:
        break