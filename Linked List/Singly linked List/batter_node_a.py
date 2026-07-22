class Node:
    def __init__(self, val):
        self.val = val       #constructor
        self.next = None


a = Node(10)
b = Node(20)

a.next = b

print(a.val)
print(b.val)
print(a.next.val)