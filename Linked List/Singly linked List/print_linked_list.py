class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


# Create Nodes
head = Node(10)
a =  Node(20)
b = Node(30)
c = Node(40)
d = Node(50)

# Connect Nodes

head.next = a
a.next = b
b.next = c
c.next = d

# Traverse the Linked List

tmp = head

while tmp is not None:
    print(tmp.val)
    tmp = tmp.next