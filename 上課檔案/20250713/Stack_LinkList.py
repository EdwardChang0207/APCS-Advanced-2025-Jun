class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def traversal(self, n): 
        if not n: return
        print(n.data)
        if not(n.next): return
        return self.traversal(n.next)
    
    def push(self, item):
        #原本為空
        if not(self.top):
            self.top = Node(item)
        #原本不為空
        else:
            n = Node(item)
            n.next = self.top
            self.top = n
    def pop(self):
        if not(s.top):
            print('Empty')
            return None
        item = s.top.data
        self.top = s.top.next
        return item
# s = Stack()
# for i in range(4):
#     s.push(i)
# s.traversal(s.top)

print(Node(3))