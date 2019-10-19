from find_factors import prime_factors
from product import product


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
    phi = num * product(uniqe_primes)  # The totient function is commonly called phi
    phi = int(round(phi))  # As phi is a whole number
    return phi
