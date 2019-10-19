def quadratic_roots(a, b, c):
    """
    Returns a tuple containg the roots of the quadratic equation ax^2+bx+c
    If the roots are imaginary then an error message is displayed and None is returned
    """
    D=(b**2)-(4*a*c)
    if D<0:
        print("Imaginary roots")
        return None
    else:
        num1=-b+(D**(1/2))
        num2=-b-(D**(1/2))
        denum=2*a
        return (num1/denum, num2/denum)
