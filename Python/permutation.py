def permutation(n, r):
	"""
	Function to calculate permuation of 'n' objects, selected 'r' at a time.
	"""
	result = 1
	for i in range(n, n-r, -1):
		result *= i
	return result
