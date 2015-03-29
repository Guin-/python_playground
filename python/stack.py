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


# write a function that uses a stack to reverse the characters in a string


def revstring(mystr):
    myStack = Stack()
    for ch in mystr:
        myStack.push(ch)
    revstr = ''
    while not myStack.isEmpty():
        revstr = revstr + myStack.pop()
    return revstr

print(revstring('apple'))
print(revstring('x'))
print(revstring('987654321'))


# write a function using a stack to check if the parentheses in a string are balanced

def parChecker(symbolStr):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolStr) and balanced:
        symbol = symbolStr[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))


