import math


def binomial_coefficient(n, k):
    """
    Finds the binomial coefficient, given n and k.
    Equals:
        n! / (k!*(n-1)!)
    """
    bin_coeff = (math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
    return bin_coeff
