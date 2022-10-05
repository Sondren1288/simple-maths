from math import sqrt as _sqrt


def per_sqr(a):
    """
    Checks if called number is a perfect square
    """
    if int(_sqrt(a) + 0.5) ** 2 == a:
        return True
    return False
    
