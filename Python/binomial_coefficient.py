import math


def binomial_coefficient(n, k):
    bin_coeff = (math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
    return bin_coeff
