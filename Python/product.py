from operator import mul as _mul
from functools import reduce as _reduce


def product(iterable):
    """
    Returns the product of an iterable
    If the list is empty, returns 1
    """
    return reduce(operator.mul, iterable, 1)
