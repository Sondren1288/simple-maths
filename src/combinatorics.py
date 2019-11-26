
def combination(n,r):
    """
    Function to calculate combination of 'n' objects, selected 'r' at a time.
    """
    N = n
    if r > n//2:
        R = n-r
    else:
        R = r
    numerator = 1
    denominator = 1
    for i in range (R, 0, -1):
        numerator *= N
        denominator *= i
        N -= 1
    return int(numerator / denominator)


def permutation(n, r):
    """
    Function to calculate permuation of 'n' objects, selected 'r' at a time.
    """
    result = 1
    for i in range(n, n-r, -1):
        result *= i
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
