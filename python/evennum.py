import sys
 
with open(sys.argv[1]) as input_file:
    data = input_file.read().rstrip()
    data = data.replace('\n', ' ').split(' ')
    for x in data:
        x = int(x)
        if x  % 2 == 0:
            print 1
        else:
            print 0
           
