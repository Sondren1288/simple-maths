import math


def point_distance(point1, point2):
    """
    Returns the distance between two points given as tuples
    """
    distance = math.sqrt(((point1[0] - point2[0])**2) +
                         ((point1[1] - point2[1])**2))
    return distance


def multidimensional_distance(point1, point2):
    """
    Return the euclidean distance between two points in multidimensional space 
    given as tuples.
    """
    # Checks if points are of the same dimension
    if len(point1) != len(point2):
        print('Points of unequal dimensions')
        return None

    dist_sq = sum( [(point1[i] - point2[i])**2 for i in range(len(point1))] )
    return math.sqrt(dist_sq)


def find_delta(a, b, c):
    """
    Function that returns the delta of a quadratic equation.
    """

    if a == 0:
        raise ValueError("a is 0! [y = ax^2 + bx + c , a != 0]")

    delta = b**2 - 4*a*c
    return delta


def find_vertex(a, b, c):
    """
    Function that returns the vertex of a parabola, given three coefficients.

    :returns: tuple
    """

    delta = find_delta(a, b, c)

    vertex = ( -b/(2*a), -(delta/(4*a)) )
    return vertex


def find_focus(a, b, c):
    """
    Function that returns the focus of a parabola, given three coefficients.

    :returns: tuple
    """

    delta = find_delta(a, b, c)

    focus = ( -b/(2*a), (1-delta)/(4*a) )
    return focus


def binomial_coefficient(n, k):
    """
    Finds the binomial coefficient, given n and k.
    Equals:
        n! / (k!*(n-1)!)
    """
    bin_coeff = (math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
    return bin_coeff


def quadratic_roots(a, b, c):
    """
    Returns a tuple containg the roots of the quadratic equation ax^2+bx+c
    If the roots are imaginary then an error message is displayed and None is returned
    """
    D = (b**2) - (4 * a * c)
    if D<0:
        print("Imaginary roots")
        return None
    else:
        num1=-b+(D**(1/2))
        num2=-b-(D**(1/2))
        denum=2*a
        return (num1/denum, num2/denum)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
