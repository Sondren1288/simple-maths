def gcd(n1, n2):
    """
    Recursive function to return the GCD of n1 and n2
    """
    if n1 == 0:
        return n2
    return gcd(n2 % n1, n1)
