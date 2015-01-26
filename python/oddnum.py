'''
Print the odd numbers from 1 to 99. One number per line.
'''

def oddnum():
    for x in range(1,100):
        if x % 2 != 0: 
            print x
oddnum()
