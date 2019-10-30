from math import pi
from math import pow
from math import sqrt

"""
Note that the standard equation for an ellipse is given by:
(x/a)^2 + (y/b)^2 = 1
        OR
(x/a)^2 + (y/b)^2 + (z/c)^2 = 1
"""

def ellipsoid_volume(a,b,c):
    """
    Returns the volume of an ellipsoid given a, b and c
    Equation: A = 4/3 pi a b c
    """
    return (4/3) * pi * a * b * c

def ellipsoid_surface_area(a,b,c):
    """
    Returns the surface area of an ellipsoid given a, b and c
    Equation: A = 4 pi ((a^p b^p + a^p c^p + b^p c^p) / 3)^(1/p)
    """
    p = 1.6075
    return 4 * pi * pow(((pow(a, p) * pow(b, p) + pow(a, p) * pow(c, p) + pow(b, p) * pow(c, p)) / 3),(1/p))

def ellipse_area(a,b):
    """
    Returns the area of an ellipse given a and b
    Equation: A = pi a b
    """
    return pi * a * b

def ellipse_circumference(a,b):
    """
    Returns the circumference of an ellipse given a and b
    Equation: C = 2 pi sqrt((a^2 + b^2) / 2)
    """
    return 2 * pi * sqrt((pow(a,2) + pow(b,2)) / 2)

# Examples
print("The volume of an ellipsoid with a=3, b=2, c=1: " + str(ellipsoid_volume(1,2,3)))
print("The surface area of an ellipsoid with a=4, b=3, c=2: " + str(ellipsoid_surface_area(4,3,2)))
print("The area of a ellipse with major axis length 3 and minor axis length 4: " + str(ellipse_area(3,4)))
print("The circumference of an ellipse with major axis length 3 and minor axis length 2: " + str(ellipse_circumference(3,2)))
