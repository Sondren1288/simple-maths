def get_fibonacci(number):
	"""
	Return fibonacci number based on given integer
	Example: get_fibonacci(6) -> 5
	"""
	
	if number==0:
		return 0
	elif number ==1:
		return 1
	else:
		return get_fibonacci(number-1)+get_fibonacci(number-2)