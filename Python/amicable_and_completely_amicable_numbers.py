def sum_proper_divisors(x):
    """
    calculate the sum of x's proper divisors
    """

    s = 1
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            s += i
    return s


def amicable_numbers(x, y):
    """"
    checking if x and y are amicable numbers
    """

    if y == sum_proper_divisors(x) and x == sum_proper_divisors(y):
        k = True
    else:
        k = False
    return k


def incompletely_amicable_numbers(x, y):
    """"
    ckecking if x and y are incompletely amicable numbers
    """

    if sum_proper_divisors(x) == sum_proper_divisors(y):
        k = True
    else:
        k = False
    return k
