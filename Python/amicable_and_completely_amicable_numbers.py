"""
Amicable numbers are numbers where the sum of the diviors equals the other nummber,
where the divisors would be every number that divides a number n except n itself (includes 1).

An example of amicable numbers:
(220, 284) 
They are amicable because the divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110, of which the sum is 284; 
and the divisors of 284 are 1, 2, 4, 71 and 142, of which the sum is 220. 
"""

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
