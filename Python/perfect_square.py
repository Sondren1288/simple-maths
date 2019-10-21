import math


def per_sqr(a):
	"""
	Checks if called number is a perfect square
	"""
	if int(math.sqrt(a) + 0.5) ** 2 == a:
		return True
	else:
		return False
	
