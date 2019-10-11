def find_primes(upper_bound):
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
