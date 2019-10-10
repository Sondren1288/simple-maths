import operator
from functools import reduce


def product(iterable):
    """
    Returns the product of an iterable
    If the list is empty, returns 1
    """
    product = reduce(operator.mul, iterable, 1)
    return product
