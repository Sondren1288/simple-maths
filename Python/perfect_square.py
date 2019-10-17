# Simple and efficient program to check entered number is a Perfect square

import math


def per_sqr(a):
    if int(math.sqrt(a) + 0.5) ** 2 == a:
        return True
    else:
        return False