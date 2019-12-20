from math import pow, sqrt


def pythagoras(p, b):
    """
    Returns the hypotenuse given the
    base and the perpendicular.
    Returns None if invalid
    """
    sq = pow(p, 2) + pow(b, 2)
    if sq > 0:
        h = sqrt(sq)
        return h
    else:
        return None
