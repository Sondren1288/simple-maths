import math

def find_primes_sieve(upper_bound):
	"""
	Returns all primess up to upper_bound (exclusive) using the sieve of Eratosthenes.
	The numbers are returned as a list.
	Example: find_primes(7) -> [2, 3, 5]
	"""

	# 1 marks a potential prime number, 0 marks a non-prime number
	# indexes 0 and 1 are not touched
	is_prime = [1] * upper_bound

	# list of found primes
	primes = []

	for n in range(2, upper_bound):
		if not is_prime[n]:
			# n was marked as non-prime
			continue

		# n is a prime number
		primes.append(n)

		# mark all multiples of n as non-prime
		# this is only necessary up to sqrt(n) because all numbers p = n * o
		# with n > sqrt(n) also the divisor o < sqrt(n)
		if n * n <= upper_bound:
			m = 2 * n
			while m < upper_bound:
				is_prime[m] = 0
				m += n

	return primes


def find_primes_old(upper_bound):
	"""
	Find primes up to upper_bound
	An attempted use of sieve
	"""
	primes = [2]

	for num in range(3, upper_bound):
		flag = True                 # Flag is used to check if prime
		for prime in primes:        # Checks for primes only
			if num % prime == 0:    # If num divided by prime == 1, then prime is a factor of num and num is not a prime
				flag = False        # Flag is False because we can see
				break
			if prime > math.sqrt(num) + 1:  # If the prime gets sufficiently close to num, it can no longer divide num
				break

		# If flag is true we add the number to primes
		if flag:
			primes.append(num)

	return primes


def prime_check(num):
	"""
	Checks if a single number is prime.
	A simple function, not a speedy solution.
	"""
	if num == 1:
		return False

	upper_bound = int(math.sqrt(num) + 1)
	for n in range(2, upper_bound):
		if num % n == 0:
			return False
	return True

