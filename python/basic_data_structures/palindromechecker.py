# Use a deque to check if a given string is a palindrome

class Deque:

    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def palindromecheck(astring):

    chrdeque = Deque()

    for ch in astring:
        chrdeque.addRear(ch)

    stillEqual = True

    while chrdeque.size() > 1 and stillEqual:
        first = chrdeque.removeFront()
        last = chrdeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual



print(palindromecheck('lsdfgrl'))
print(palindromecheck('racecar'))
