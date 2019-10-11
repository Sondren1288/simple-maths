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



def factorialRecursion(n):
    #The factorial of a number, done with Recursion.
    #Limit set to 0, to cancel the Recursion-Loop

    if n < 1:
        return 1
    return factorialRecursion(n-1) * n
