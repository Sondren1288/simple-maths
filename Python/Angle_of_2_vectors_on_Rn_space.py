import math


def inner_p_s(u, v):  
    """
    
    Calculate the Inner product space of the 2 vectors
    """
    s = 0
    if len(u) != len(v):
        s = -1
    else:
        for i in range(len(u)):
            s += u[i]*v[i]
    return s


def calc_norm(k):          
    """ 
    
    Calculate the Euclidean norm On an n-dimensional Euclidean space Rn
    """

    c = 0
    for i in range(len(k)):
        c += k[i] ** 2
    x = math.sqrt(c)
    return x


def calc_angle(m, n):            
    """
    
    Calculate the cosθ, where θ is the angle between 2 vectors, m and n
    """

    if inner_p_s(m, n) == -1:
        print('Error! The 2 vectors should belong on the same space Rn!')
    elif inner_p_s(m,n) == 0:
        print('The cosine of the two vectors is 0, so these vectors are orthogonal! ')
    else:
        angle = (inner_p_s(m, n))/(calc_norm(m) * calc_norm(n))
        return angle
