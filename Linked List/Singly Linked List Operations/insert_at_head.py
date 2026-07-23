class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_at_tail(head, v):
    new_node = Node(v)

    if head is None:
        print("\nInserted at head\n")
        return new_node

    tmp = head
    while tmp.next is not None:
        tmp = tmp.next

    tmp.next = new_node

    print("\nInserted at tail\n")
    return head


def print_linked_list(head):
    print("\nYour Linked List:", end=" ")

    tmp = head
    while tmp is not None:
        print(tmp.val, end=" ")
        tmp = tmp.next

    print("\n")


def insert_at_position(head, pos, v):
    new_node = Node(v)

    tmp = head

    for i in range(1, pos):
        tmp = tmp.next

    new_node.next = tmp.next
    tmp.next = new_node

    print(f"\nInserted at position {pos}\n")

    return head


def insert_at_head(head, v):
    new_node = Node(v)

    new_node.next = head
    head = new_node

    print("\nInserted at head\n")

    return head


head = None

while True:
    print("Option 1: Insert at Tail")
    print("Option 2: Print Linked List")
    print("Option 3: Insert at any Position")
    print("Option 4: Insert at Head")
    print("Option 5: Terminate")

    op = int(input())

    if op == 1:
        value = int(input("Please enter value: "))
        head = insert_at_tail(head, value)

    elif op == 2:
        print_linked_list(head)

    elif op == 3:
        pos = int(input("Enter position: "))
        value = int(input("Enter value: "))

        if pos == 0:
            head = insert_at_head(head, value)
        else:
            head = insert_at_position(head, pos, value)

    elif op == 4:
        value = int(input("Enter value: "))
        head = insert_at_head(head, value)

    elif op == 5:
        break