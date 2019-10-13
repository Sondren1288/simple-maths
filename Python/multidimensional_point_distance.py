import math

def multi_dimensional_distance(point1, point2):
    """
    Return the euclidean distance between two points in n-dimensional space 
    given as tuples.
    """

    dist_sq = sum([(point1[i] - point2[i])**2 for i in range(len(point1))])
    return math.sqrt(dist_sq)
