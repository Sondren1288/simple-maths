from functools import reduce
import operator
import math


def product(iterable):
	"""
	Returns the product of an iterable
	If the list is empty, returns 1
	"""
	product = reduce(operator.mul, iterable, 1)
	return product


def prime_check(num):
	"""
	Checks if a number is prime.
	A simple function, not a speedy solution.
	"""
	if num == 1:
		return False

	upper_bound = int(math.sqrt(num) + 1)
	for n in range(2, upper_bound):
		if num % n == 0:
			return False
	return True


def find_primes(upper_bound):
	"""
	Find primes up to upper_bound
	An attemted use of sieve
	"""
	primes = [2]


	for num in range(3, upper_bound):
		flag = True 					# Flag is used to check if prime
		for prime in primes:
			if num % prime == 0:			# If num divided by prime == 1, then prime is a factor of num and num is not a prime
				flag = False			# Flag is False because we can see 
				break
			if prime > math.sqrt(num) + 1: 		# If the prime gets sufficiently close to num, it can no longer divide num
				break

		# If flag is true we add the number to primes
		if flag:
			primes.append(num)

	return primes




