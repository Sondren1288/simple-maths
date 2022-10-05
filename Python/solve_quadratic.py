from math import sqrt


def quadratic_equation(a, b, c):
    """
    solution for quadratic equation
    a*x**2 + b*x + c = 0
    """
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None, None
    elif d == 0:
        x1 = -b / (2 * a)
        return x1, x1
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    return x1, x2
