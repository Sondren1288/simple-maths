from math import sqrt
from math import pi
from math import pow


# Squares
def area_square(n):
    """
    Takes the length of a square and returns the
    area of the square, given by n*n
    """
    area = n*n
    return area


def perimeter_square(n):
    """
    Take the length of the side of a square
    and calculate the perimeter, given by 4*n.
    """
    perimeter = 4*n
    return perimeter


# Triangles
def area_triangle(a, b, c):
    """
    This function applies the heron's formula to calculate
    the area of traingle, it takes the dimensions of three sides
    and returns the value of area in respective square dimensions
    """
    s = (a + b + c) / 2 # Semi-perimeter
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area


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


# Circles
def area_circle(radius):
    """
    Calculates the area of a circle given the radius
    """
    return pi * pow(radius,2)


# Spheres
def volume_sphere(radius):
    """
    Returns the volume of a sphere given a radius
    Equation: V = 4/3 pi r^3
    """
    return (4/3) * pi * pow(radius,3)


def area_sphere(radius):
    """
    Returns the surface area of a sphere given a radius
    Equation: SA = 4 pi r^2
    """
    return 4 * pi * pow(radius,2)


# Cylinders
def area_cylinder(r, h):
    """
    Takes in the radius and height of a cylinder
    and returns the area of the surface of the cylinder
    """
    circle = pi * r ** 2
    # The 2*r is neccessary as we need the diameter
    body = pi * 2 * r * h
    area = 2 * circle + body
    return area


def volume_cylinder(r, h):
    """
    Finds the volume of a cylinder given 
    radius and height.
    """
    circle = pi * r ** 2
    volume = circle * h
    return volume
