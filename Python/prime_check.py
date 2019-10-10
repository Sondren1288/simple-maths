import math


def prime_check(num):
    """
    Checks if a number is prime.
    A simple function, not a speedy solution.
    """
    if num == 1:
        return False

    upper_bound = int(math.sqrt(num) + 1)
    for n in range(2, upper_bound):
        if num % n == 0:
            return False
    return True
