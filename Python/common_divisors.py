def gcd(n1, n2):
    """
    Non-Recursive function to return the GCD of n1 and n2
    """
    if n1 < n2:
        n1, n2 = n2, n1
    while n1 % n2:
        n1, n2 = n2, n1 % n2
    return n2


def gcd_recursive(n1, n2):
    """
    Recursive function to return the GCD of n1 and n2
    """
    if n1 == 0:
        return n2
    return gcd(n2 % n1, n1)


def lcm(n1, n2):
    """
    Function to return the lcm of two numbers
    """
    return (n1 * n2) / gcd(n1, n2)