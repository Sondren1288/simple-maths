def factorial(num):
    """
    The factorial of a number.
    On average barely quicker than product(range(1, num))
    """
    # Factorial of 0 equals 1
    if num == 0:
        return 1

    # if not, it is the product from 1...num
    # product = 1
    # for integer in range(1, num + 1):
    #     product *= integer

    #implementing recursion
    return num * factorial(num-1)
