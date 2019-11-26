import math
from array import product_of_list


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
    primes = find_primes_sieve(num)  # Finds all primes that might be a factor
    factors = []

    for prime in primes:

        if prime >= num + 1:    # If prime is bigger than the number, it is no longer divisible
            break               # So for long lists, quitting earlier is faster

        while num % prime == 0:
            num = num // prime      # Divides the number by the prime, so that we can see how many times
            factors.append(prime)   # a number is divisible by a prime

    return factors


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
    uniqe_primes = [(1 - 1 / p) for p in set(prime_factors(num))]
    phi = num * product_of_list(uniqe_primes)  # The totient function is commonly called phi
    phi = int(round(phi))  # As phi is a whole number
    return phi


if __name__ == '__main__':
    import doctest
    doctest.testmod()
