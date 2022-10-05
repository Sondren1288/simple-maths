# Perm function is built-in permutation function
from math import factorial, perm


def combination(n, r):
    """
    Function to calculate combination of 'n' objects, selected 'r' at a time.
    """
    N = n
    if r > n // 2:
        R = n - r
    else:
        R = r
    numerator = 1
    denominator = 1
    for i in range(R, 0, -1):
        numerator *= N
        denominator *= i
        N -= 1
    return int(numerator / denominator)


def combinations(n, r):
    # Number of combinations (order doesn't matters) of n things taken r at a single time
    return perm(n, r) / factorial(r)