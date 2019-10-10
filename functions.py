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


def prime_factors(num):
	"""
	Finds the smallest primes that divide a number.
	For unique primes, turn the list into a set.
	Example: 	120 / 2 = 60
				60 / 2 = 30
				30 / 2 = 15
				15 / 3 = 5
				5 is prime.
				returns [2, 2, 2, 3, 5]
	"""
	primes = find_primes(num) # Finds all primes that might be a factor
	factors = []

	for prime in primes:

		if prime >= num + 1: 	# If prime is bigger than the number, it is no longer divisible
			break				# So for long lists, quitting earlier is faster

		while num % prime == 0:
			num = num // prime 	# Divides the number by the prime, so that we can see how many times
			factors.append(prime) # a number is divisible by a prime

	return factors


def factorial(num):
	"""
	The factorial of a number.
	On average barely quickar than product(range(1, num))
	"""
	# Factorial of 0 equals 1
	if num == 0:
		return 1

	#if not, it is the product from 1...num
	product = 1
	for integer in range(1, num + 1):
		product *= integer
	return product


def zeros(dimensions):
	"""
	Attempted clone of numpy zeros.
	Not as quick, but might be useful if long lists are desired
	and numpy not available.
	"""
	x = y = None
	try:
		y, x = dimensions 	# If it cannot unpack it as tuple, it will fail
	except TypeError:
		x = dimensions		# If it fails, it will standard to 1 row
		y = 1
	
	zeros = []
	if y == 1:
		zeros += [0]*x
	else:
		for row in range(y): 	# Makes rows with columns of 0
			zeros.append([0]*x)
	
	return zeros


def louville_distance(precision):
	"""
	Finds the distance between in zeroes between 2 '1's in the 
	louville number. 
	Will return distances, so if you sum earlier numbers together
	you get the index at which there would have been a '1'
	"""
	precision += 1 		# To get far enouh
	distances = []

	for index in range(1, precision):
		try:
			distances.append(factorial(index) - factorial(index - 1))
		except IndexError:
			break

	distances[0] = 1 # Because of the way the list is structured
	return distances


def point_distance(point1, point2):
	"""
	Returns the distance between two points given as tuples
	"""
	distance =  math.sqrt( ((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2) )
	return distance

def gcd(n1, n2): 
	"""
	Recursive function to return the GCD of n1 and n2
	"""
	if n1 == 0: 
		return n2 
	return gcd(n2 % n1, n1) 

def lcm(n1, n2):
	"""
	Function to return the lcm of two numbers
	"""
	return (n1*n2) / gcd(n1,n2)

def totient(num):
	"""
	Counts the numbers that are relative prime to the number.
	This means that if a number 'x' has common divisors with another number 'a' lower than itself,
	it is, 'a' is not relative prime to 'x'.
	This means that if a number is prime, its totient function is its value - 1, as 
	all numbers lower than the number itself is relative prime to the number.
	An example: totient(9):
				1, 2, 4, 5, 7, 8 are all relative prime
				3, 6, and 9 have at least one common divisor with 9
				returns 6, as there are 6 numbers relative prime to 9
	
	If you visit 'https://en.wikipedia.org/wiki/Euler%27s_totient_function'
	this function uses the function described under euler's product formula.
	"""
	# set(prime_factors(num)) to get only unique primes.
	# it is the (1 - 1/p) part from the wiki-page
	uniqe_primes = [(1 - 1/p) for p in set(prime_factors(num))]
	phi = num * product(uniqe_primes) 	# The totient function is commonly called phi
	phi = int(round(phi)) 				# As phi is a whole number
	return phi

def nCr(n, r):
    """
    A binomial coefficient gives the number of ways, disregarding order, that r objects can be chosen from among n objects;
    more formally, the number of r-element subsets (or r-combinations) of an n-element set.
    nCr = (n!) / (r! * (n-r)!)
    :param n:
    :param r:
    :return: nCr Integer
    """
    return factorial(n) / (factorial(r) * factorial(n - r))

