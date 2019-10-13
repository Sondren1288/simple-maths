def fib(n):
 	"""
 	Returns the nth fibonacci number
 	"""
 	if n < 0:
 		return (fib(n + 2) - fib(n + 1))
 	elif n < 2:
 		return n
 	return fib(n-2) + fib(n-1)