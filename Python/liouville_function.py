# -*- coding: utf-8 -*-

from prime_factor import prime_factors

def liouville_function(n):
    """
    For a positive number n, the Liouville function λ(n) returns (-1)**Ω(n)
    where Ω(n) is the number of all the prime factors of n (counted with multiplicity),
    being Ω(1) = 0
    Example: liouville_function(120) -> 
        120 has five prime factors [2, 2, 2, 3, 5] so (-1)**5 = -1
    """
    result = 0    
    num_factors = 0
    if n > 1:
        num_factors = max(1, len(prime_factors(n)))
    result = (-1)**num_factors
    return result
