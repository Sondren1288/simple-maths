# Finds the area/volume of a cylinder given the height and radius.

import math


def areaOfCylinder(r, h):
    return 2 * (math.pi * r * h) + 2 * (math.pi * r**2)


def volumeOfCylinder(r, h):
    return math.pi * r**2 * h