# Implement a deque data structure.
# Deque can have items removed and added from both ends
# Functionality of a stack and a queue - does not require LIFO & FIFO orderings

class Deque:

    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self,item):
        return self.items.pop()

    def removeRear(self,item):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


