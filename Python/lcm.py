from gcd import gcd


def lcm(n1, n2):
    """
    Function to return the lcm of two numbers
    """
    return (n1 * n2) / gcd(n1, n2)
