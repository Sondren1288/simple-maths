def AreaTriangle(a, b, c):
    """
    Returns the area of any triangle
    """
    s=(a+b+c)/2
    ar=(s*(s-a)*(s-b)*(s-c))**(1/2)
    return ar
