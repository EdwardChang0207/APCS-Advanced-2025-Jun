class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def traversal(self, n): #l.head -> n=l.head.next -> l.head.next.next
        if not n: return
        print(n.data)
        if not(n.next): return
        return self.traversal(n.next)
    
    def append(self, n, item):
        if not(n): self.head = Node(item)
        if n.next: return self.append(n.next, item)
        n.next = Node(item)

    def pop(self, n):#取出最後一項
        if not(n): return
        if not(n.next.next):
            item = n.next.data
            n.next = None
            return item
        return self.pop(n.next)

#1 -> 2 -> 3 -> 4

a, b, c, d = Node(1), Node(2), Node(3), Node(4)
l = Linked_list()
l.head = a
a.next = b
b.next = c

#traversal
# print(l.head.data)
# print(l.head.next.data)
# print(l.head.next.next.data)
# print(l.head.next.next.next.data)

l.traversal(l.head)

#append
l.append(l.head, 8)
l.traversal(l.head)
a = l.pop(l.head)
print(a)
l.traversal(l.head)




