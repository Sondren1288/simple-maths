from math import factorial


def permutations(n, r):
    """
    Function to calculate permuation of 'n' objects, selected 'r' at a time.
    """
    result = 1
    for i in range(n, n-r, -1):
        result *= i
    return result


def permutations_(n, r):
    """
    Number of permutations (order matters) of n things taken r at a single time
    """
    return factorial(n) / factorial(n-r)
