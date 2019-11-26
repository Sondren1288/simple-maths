import math
import operator
import collections
import functools


def product_of_list(iterable):
    """
    Returns the product of an iterable
    If the list is empty, returns 1
    """
    product_ = functools.reduce(operator.mul, iterable, 1)
    return product_
    

def var_sum(*args):
    """
    Variable argument sum
    """
    total = 0
    for arg in args:
        try:
            arg+1
            total += arg
        except TypeError: # invlid input hence return early
            return
    return total


def sum_of_n_natual_numbers(n):
    """
    Returns sum of first n natural numbers
    """
    try:
        n+1
    except TypeError: # invlid input hence return early
        return 
    if n < 1: # invlid input hence return early
        return 

    return n*(n+1) // 2


def sum_of_n_even_numbers(n):
    """
    Returns sum of first n even numbers
    """
    try:
        n+1
    except TypeError: # invlid input hence return early
        return 
    if n < 0: # invlid input hence return early
        return 

    return n*(n+1)


def sum_of_n_odd_numbers(n):
    """
    Returns sum of first n odd numbers
    """
    try:
        n+1
    except TypeError: # invlid input hence return early
        return 
    if n < 0: # invlid input hence return early
        return 

    return n*n


def sum_of_square_of_n_numbers(n):
    """
    The sum of squares of first n natural numbers
    ∑ n^2 = 1^2 + 2^2 + 3^2 +....+ n^2
    """
    try:
        n+1
    except TypeError: # invlid input hence return early
        return 
    if n < 0: # invlid input hence return early
        return 

    return n * (n + 1) * (2 * n + 1) // 6


def unique_elements(input_list):
    """
    Functions to find unique elements from a list of given numbers.
    
    :param input_list: list or tuple

    >>> unique_elements([1, 0, 1, 0, 1, 2])
    [0, 1, 2]
    """
    return list(set(input_list))


def frequency(input_list):
    """
    Finds the occurances of elements in a list.
    Works with numbers not consisting of numbers as well.

    :param input_list: list or tuple

    >>> frequency([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    Counter({4: 4, 3: 3, 2: 2, 1: 1})
    """
    return collections.Counter(input_list)


def rms(list_):
    """
    Finds the root mean square of a list of numbers.
    """

    result = 0
    for num in list_:
        result += num*num
	
    result = result / len(list_)
    result = math.sqrt(result)
    return result


def zeros(dimensions):
    """
    Not as quick, but might be useful if long lists are desired
    and numpy not available.

    :param dimensions: tuple, list or int

    >>> zeros(3)
    [0, 0, 0]
    >>> zeros([3, 4])
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    x = None
    y = None

    if isinstance(dimensions, int):
        x = dimensions
        y = 1
    elif isinstance(dimensions, (list, tuple,)):
        if len(dimensions) > 2:
            raise Exception('Zeros can only be 2 dimensional.')

        y, x = dimensions if len(dimensions) != 1 else (1, dimensions[0],)   # y standards to 1

    zero_row = [0 for _ in range(x)]

    if y == 1:
        return zero_row

    return [zero_row for _ in range(y)]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
