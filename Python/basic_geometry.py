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
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


# Circles
def area_circle(radius):
    """
    Calculates the area of a circle given the radius
    """
    return pi * pow(radius,2)
