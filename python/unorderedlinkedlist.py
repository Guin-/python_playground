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

