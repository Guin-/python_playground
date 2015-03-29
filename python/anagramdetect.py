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

def anagramSolution2(s1, s2):
    pass

