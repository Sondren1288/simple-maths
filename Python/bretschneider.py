import math


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
