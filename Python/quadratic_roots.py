from math import sqrt


def quadratic_roots(a, b, c):
    """
    Returns a tuple containg the roots of the quadratic equation ax^2+bx+c
    If the roots are imaginary then an error message is displayed and None is returned
    """
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        print("Imaginary roots")
        return None
    else:
        num1 = -b + ( sqrt(d) )
        num2 = -b - ( sqrt(d) )
        denum = 2*a
        return (num1/denum, num2/denum)
