# y = ax^2 + bx + c  (a != 0)

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

    returns: tuple
    """

    delta = find_delta(a, b, c)

    vertex = ( -b/(2*a), -(delta/(4*a)) )
    return vertex


def find_focus(a, b, c):
    """
    Function that returns the focus of a parabola, given three coefficients.

    returns: tuple
    """

    delta = find_delta(a, b, c)

    focus = ( -b/(2*a), (1-delta)/(4*a) )
    return focus
