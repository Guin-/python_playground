'''
Use recursion to handle arbitrarily shaped structures. 
'''

def sumtree(L):
	tot = 0
	print L
	for x in L:						# For each item at this level
		if not isinstance(x, list):			# if item is not a list
			tot += x				# Add these numbers directly
			
		else:
			tot += sumtree(x)			# Recur for each sublist
			 
	return tot


#L = [1, [2, [3, 4], 5], 6, [7, 8]]


#print (sumtree(L))

print (sumtree([1, [2, [3, [4, [5], ]]]]))

