# Write a boolean function that takes in two strings
# (they are of equal length and composed of lowercase alphabetic chars)
# and returns whether they are anagrams.

## Solution 1
# Checking Off
# Check if each character in first string is in second string
# Found char will be replaced with None value.
# Convert string 2 to list so that it is mutable.

def anagramSolution1(s1, s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 += 1

    return stillOK

print(anagramSolution1('abcd', 'dbca'))

## Solution 2
# Sort and Compare
# Convert strings to list and run sort method
# Same Order of magnitude as the sorting process

def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False

    return matches
print (anagramSolution2('bdefk', 'fedcb'))

## Solution 3
# Count and compare
# Count number of times each character appears
# list of 26 counters
# T(n) = 2n + 26
# linear 0(n)
# sacrificed space to gain time.
# This is insignificant for this case as there are only 26 characters.

def anagramSolution3(s1, s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1


    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    stillOK = True
    while j <26 and stillOK:
        if c1[j] == c2[j]:
            j +=1
        else:
            stillOK = False

    return stillOK

print(anagramSolution3('apple', 'plepa'))
