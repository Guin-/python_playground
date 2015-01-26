from sys import argv

script, filename = argv

with open(filename, 'r') as f:
    for line in f:
        print line.lower()



