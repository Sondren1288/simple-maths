def factorial(num):
	"""
	The factorial of a number.
	On average barely quicker than product(range(1, num))
	Recursive implementation
	"""
	# Factorial of 0 equals 1
	if num == 0:
		return 1
	else :
		return num*factorial(num-1)

