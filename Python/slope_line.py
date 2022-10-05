import math 

def find_slope(point1, point2):
    """ Returns the slope of the line form by the two points """

    slope = (point2[1] - point1[1])/ (point2[0] - point1[0])
    return slope

