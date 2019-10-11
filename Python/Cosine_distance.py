'''
Program to compute Cosine Distance between an two given vectors
@params
	input: two vectors (lists in python
	output: similarity score
'''
import math
from operator import mul
def dot_product2(v1, v2):
    return sum(map(mul, v1, v2))


def vector_cos5(v1, v2):
    prod = dot_product2(v1, v2)
    len1 = math.sqrt(dot_product2(v1, v1))
    len2 = math.sqrt(dot_product2(v2, v2))
    return prod / (len1 * len2)
    
#Usage
#Score = vector_cos5([1,2,3],[3,2,1])
