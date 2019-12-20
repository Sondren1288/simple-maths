import math
import random

def estimate(total_points=1E5):
    """
    Estimates pi by using assuming random points on a square
    with sides 2 inscribing a circle with radius 1.
    By dividing the ones in the circle / total point * 4, we get an
    estimate for pi.
    
    Taken from 'Doing Math with Python'by Amit Saha
    """
    radius = 1
    center = (radius, radius)

    in_circle = 0
    for i in range(total_points):
        x = random.uniform(0, 2 * radius)
        y = random.uniform(0, 2 * radius)
        p = (x, y)
        # distance from circle's center
        d = math.sqrt((p[0] - center[0])**2 + (p[1] - center[1])**2)
        if d <= radius:
            in_circle += 1
    return (in_circle / total_points) * 4
