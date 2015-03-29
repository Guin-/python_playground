# Implementing a stack
# comments for implementing stack where beginning of list is the top
# if using end of list as top of stack push and pop are 0(1)
# if using beginning of list as top of stack, push and pop are O(n)
# less efficient, depend on size of stack

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item) # self.items.insert(0, item)

    def pop(self):
        return self.items.pop() # return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items)-1] # return self.items[0]

    def size(self):
        return len(self.items)

s = Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.2)
s.pop()
s.pop()
print(s.size())






