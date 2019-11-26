import math


def find_factors(n):
    """
    Finds a list of factors of a number
    """
    factList = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0):
            factList.add(i)
            factList.add(n // i)
    return sorted(factList)


def find_divisors(n):
    """
    Find all the divisors of a positive number n, including 1 and n.
    Example: find_divisors(12) -> {1, 2, 3, 4, 6, 12}
    """
    divisors = {1}
    for i in range(2, math.ceil(n**0.5) + 1):
        if n%i == 0:
            divisors.add(i)
            divisors.add(n//i)
    divisors.add(n)
    return divisors


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


def perfect_square(a):
    """
    Checks if called number is a perfect square
    """
    if int(math.sqrt(a) + 0.5) ** 2 == a:
        return True
    else:
        return False


def factorial(num):
    """
    The factorial of a number.
    On average barely quicker than product(range(1, num))
    """
    # Factorial of 0 equals 1
    if num == 0:
        return 1

    # if not, it is the product from 1...num
    product = 1
    for integer in range(1, num + 1):
        product *= integer
    return product


def louville_distance(precision):
    """
    Finds the distance between in zeroes between 2 '1's in the
    louville number.
    Will return distances, so if you sum earlier numbers together
    you get the index at which there would have been a '1'
    """
    precision += 1  # To get far enough
    distances = []

    factorial_cache = {}

    def factorial_(num):
        if num not in factorial_cache:
            factorial_cache[num] = factorial(num)
        return factorial_cache[num]

    for index in range(1, precision):
        distances.append(factorial(index) - factorial(index - 1))

    distances[0] = 1  # Because of the way the list is structured
    return distances


def get_common_divisors(n1, n2):
    """
    Non-Recursive function to return the GCD of n1 and n2
    """
    if n1 < n2:
        n1, n2 = n2, n1
    while n1 % n2:
        n1, n2 = n2, n1 % n2
    return n2


def get_common_divisors_recursive(n1, n2):
    """
    Recursive function to return the GCD of n1 and n2
    """
    if n1 == 0:
        return n2
    return get_common_divisors(n2 % n1, n1)


def get_least_common_divisors(n1, n2):
    """
    Function to return the lcm of two numbers
    """
    return (n1 * n2) / get_common_divisors(n1, n2)


def armstrong_number(number):
    """
    Check if number is Armstrong number
    """
    calc = number
    sum_ = 0
    while calc > 0:
        dig = calc % 10
        sum_ += dig ** 3
        calc //= 10
    if number == sum_:
        return True
    else:
        return False


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
    Calculate the sum of x's proper divisors
    """

    s = 1
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            s += i
    return s


def amicable_numbers(x, y):
    """"
    Checking if x and y are amicable numbers
    """

    if y == sum_proper_divisors(x) and x == sum_proper_divisors(y):
        k = True
    else:
        k = False
    return k


def incompletely_amicable_numbers(x, y):
    """"
    Checking if x and y are incompletely amicable numbers
    In other words, checks if the sum of the divisors is equal
    """

    if sum_proper_divisors(x) == sum_proper_divisors(y):
        k = True
    else:
        k = False
    return k


if __name__ == '__main__':
    import doctest
    doctest.testmod()
