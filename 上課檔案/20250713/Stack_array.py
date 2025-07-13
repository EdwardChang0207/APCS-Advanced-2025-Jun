'''s = ['' for _ in range(5)]
top = 0

for i in range(3):
    top += 1
    s[top] = i
    print(f"s:{s}")
    print(f'top:{top}')

for i in range(2):
    item = s[top]
    top -= 1
    print(f"s:{s}")
    print(f'top:{top}')
    print(f'item:{item}')

for i in range(3,5):
    top += 1
    s[top] = i
    print(f"s:{s}")
    print(f'top:{top}')
'''

class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.data = ['' for _ in range(size)]
    
    def push(self, item):
        if self.top == self.size-1:
            print('Full')
            return
        #1 top向上 
        self.top += 1
        #2 item放到第top項
        self.data[self.top] = item

    def pop(self):
        if self.top == 0: 
            print('Empty')
            return
        #1 item拿出來
        item = self.data[self.top]
        #2 top下降
        self.top -= 1
        return item
    
s = Stack(5)
print(s.size)
print(s.top)
print(s.data)

for i in range(6):
    s.push(i)
    print(s.size)
    print(s.top)
    print(s.data)

# for i in range(6):
#     i = s.pop()
#     print(i)
#     print(s.size)
#     print(s.top)
#     print(s.data)