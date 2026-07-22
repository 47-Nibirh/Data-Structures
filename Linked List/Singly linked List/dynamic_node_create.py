class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


head = Node(10)
a = Node(30)

head.next = a

print(head.val)
print(a.val)
print(head.next.val)