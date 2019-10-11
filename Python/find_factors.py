def find_factors(n):
    """
    Finds a list of factors of a number
    """
    factList = []
    for i in range(1, int(n ** 0.5) + 1):
        if (n % i == 0):
            factList.append(i)
            factList.append(n // i)
    return sorted(set(factList))
