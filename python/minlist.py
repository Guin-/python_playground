# O(n^2)

import time
from random import randrange

def findMin(alist):
    overallMin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallMin = i
    return overallMin

# O(n) linear search

def findMin(alist):
    minsofar = alist[0]
    for x in alist:
        if x < minsofar:
            minsofar = x
    return minsofar



for listSize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print (findMin(alist))
    end = time.time()
    print ("size: %d time: %f" % (listSize, end-start))



