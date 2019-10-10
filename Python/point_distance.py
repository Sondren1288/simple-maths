import math


def point_distance(point1, point2):
    """
    Returns the distance between two points given as tuples
    """
    distance = math.sqrt(((point1[0] - point2[0])**2) +
                         ((point1[1] - point2[1])**2))
    return distance
