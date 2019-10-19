from find_primes import find_primes_sieve


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
