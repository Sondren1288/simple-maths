import math


def point_distance(point1, point2):
    """
    Returns the distance between two points given as tuples
    """
    distance = math.sqrt(((point1[0] - point2[0])**2) +
                         ((point1[1] - point2[1])**2))
    return distance


def multidimensional_distance(point1, point2):
    """
    Return the euclidean distance between two points in multidimensional space 
    given as tuples.
    """
    # Checks if points are of the same dimension
    if len(point1) != len(point2):
        print('Points of unequal dimensions')
        return None

    dist_sq = sum( [(point1[i] - point2[i])**2 for i in range(len(point1))] )
    return math.sqrt(dist_sq)
