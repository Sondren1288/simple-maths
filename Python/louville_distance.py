from factorial import factorial


def louville_distance(precision):
	"""
	Finds the distance between in zeroes between 2 '1's in the
	louville number.
	Will return distances, so if you sum earlier numbers together
	you get the index at which there would have been a '1'
	"""
	precision += 1  # To get far enough
	distances = []

	factorial_cache = {}

	def factorial_(num):
		if num not in factorial_cache:
			factorial_cache[num] = factorial(num)
		return factorial_cache[num]

	for index in range(1, precision):
		distances.append(factorial(index) - factorial(index - 1))

	distances[0] = 1  # Because of the way the list is structured
	return distances
