from math import pi
from math import pow

def sphere_volume(radius):
    """
    Returns the volume of a sphere given a radius
    Equation: V = 4/3 pi r^3
    """
    return (4/3) * pi * pow(radius,3)

def sphere_surface_area(radius):
    """
    Returns the surface area of a sphere given a radius
    Equation: SA = 4 pi r^2
    """
    return 4 * pi * pow(radius,2)

# Examples
print("The volume of a sphere with radius 3 is: " + str(sphere_volume(3)))
print("The surface area of a sphere with radius 5 is: " + str(sphere_surface_area(5)))
