import math


def find_primes(upper_bound):
    """
    Find primes up to upper_bound
    An attempted use of sieve
    """
    primes = [2]

    for num in range(3, upper_bound):
        flag = True  # Flag is used to check if prime
        for prime in primes:
            if num % prime == 0:  # If num divided by prime == 1, then prime is a factor of num and num is not a prime
                flag = False  # Flag is False because we can see
                break
            if prime > math.sqrt(num) + 1:  # If the prime gets sufficiently close to num, it can no longer divide num
                break

        # If flag is true we add the number to primes
        if flag:
            primes.append(num)

    return primes
