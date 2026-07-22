class Node:
    def __init__(self):
        self.val = None
        self.next = None


a = Node()
b = Node()

a.val = 10
b.val = 20


a.next = b
b.next = None

print(a.val)
print(b.val)
print(a.next.val)