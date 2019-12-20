# -*- coding: utf-8 -*-

from math import ceil


def find_divisors(n):
    """
    Find all the divisors of a positive number n, including 1 and n.
    Example: find_divisors(12) -> {1, 2, 3, 4, 6, 12}
    """
    divisors = {1}
    for i in range(2, ceil(n**0.5)+1):
        if n%i == 0:
            divisors.add(i)
            divisors.add(n//i)
    divisors.add(n)
    return divisors
