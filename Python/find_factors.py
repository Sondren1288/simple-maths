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
