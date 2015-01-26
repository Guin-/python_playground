'''
Write a program that prints out the numbers 1 to 100 (inclusive). If the number is divisible by 3, print Crackle instead of the number. If it's divisible by 5, print Pop. If its divisible by both 3 and 5, print CracklePop.
'''


def CracklePop():
	for x in range(1, 101):
		if x % 3 == 0 and x % 5 == 0:
			print 'CracklePop'
		elif x % 3 == 0:
			print 'Crackle'
		elif x % 5 == 0:
			print 'Pop'
		else:
			print x

print CracklePop()
