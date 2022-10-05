from math import factorial


def binomial_coefficient(n, r):
    """
    A binomial coefficient gives the number of ways, disregarding order, that r objects can be chosen from among n objects;
    more formally, the number of r-element subsets (or r-combinations) of an n-element set.
    nCr = (n!) / (r! * (n-r)!)
    :param n:
    :param r:
    :return: nCr Integer
    """
    bin_coeff = factorial(n) // (factorial(r) * factorial(n - r))
    return bin_coeff
