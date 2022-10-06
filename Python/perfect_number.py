# -*- coding: utf-8 -*-

from find_divisors import find_divisors


def perfect_number(n):
    """
    Check if a positive integer is a perfect number.
    A perfect number is a positive integer that is equal 
    to the sum of its positive divisors, excluding the number itself.
    Example: perfect_number(6) -> True
        since the divisors of 6 (excluding itself) are 1 + 2 + 3
    """
    divisors = find_divisors(n)
    divisors.remove(n)
    sum_divisors = sum(divisors)
    return sum_divisors == n
