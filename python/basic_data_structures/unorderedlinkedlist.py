# Implement an unordered linked list

# Basic building block for a linked list is a node.
# A Node object must contain the list item itself and
# a reference to the next node
# Initial next set to None is referred to as 'grounding the node'

class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

temp = Node(93)
temp.getData()

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

# Create two external references, current and previous,
# so that previous traverses the list one node behind
# current to solve the issue of not being able to
# move backwards through the list.
# Known as inch-worming. Previous must catch up to
# current before current can move a node ahead.

    def remove(self,item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())





myList = UnorderedList()






