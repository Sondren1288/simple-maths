import math


def area_circle(radius):
    """
    Calculates the area of a circle given the radius
    """
    return math.pi * math.pow(radius, 2)


def area_of_triangle(a, b, c):
    """
    This function applies the heron's formula to calculate
    the area of traingle, it takes the dimensions of three sides
    and returns the value of area in respective square dimensions.

    :param a: int
    :param b: int
    :param c: int

    >>> area_of_triangle(10, 30, 30)
    147.9019945774904
    """
    s = (a + b + c) / 2  # Semi-perimeter
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def bretschneider(a, b, c, d, ab, cd):
    """
    Calulate the area of a quadrilateral with the length of the four sides a,b,c,d and 
    the degrees of an opposite pair of angles.
    Uses the Bretschneider's formula.
    Can be used on any quadriliteral as long as all lengths are known
    and as long as to opposite angles are known.
    """
    p = (a + b + c + d) * 0.5
    radsum = (ab + cd) * 3.1415926 / 360    # Should this be (pi / 180)?
    area = ((p - a) * (p - b) * (p - c) * (p - d) - a*b*c*d*math.cos(radsum)**2)**0.5 
    return area


if __name__ == '__main__':
    import doctest
    doctest.testmod()
