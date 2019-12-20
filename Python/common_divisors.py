def gcd(n1, n2):
    """
    Non-Recursive function to return the 
    GCD (greatest common divisor) of n1 and n2
    """
    if n1 < n2:
        n1, n2 = n2, n1
    while n1 % n2:
        n1, n2 = n2, n1 % n2
    return n2


def gcd_recursive(n1, n2):
    """
    Recursive function to return the 
    GCD (greatest common divisor) of n1 and n2
    """
    if n1 == 0:
        return n2
    return gcd(n2 % n1, n1)


def lcm(n1, n2):
    """
    Function to return the lcm 
    (least common multiple) of two numbers
    """
    return (n1 * n2) / gcd(n1, n2)


def lcm_trial(a,b):
    """
    Finds the least common multiple of 
    2 numbers without using GCD
    """
    greater = b if a < b else a
    while(True):
        if ((greater % a == 0) & (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
