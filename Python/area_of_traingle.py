import math
def area(a, b, c):
    """
    This function applies the heron's formula to calculate
    the area of traingle, it takes the dimensions of three sides
    and returns the value of area in respective square dimensions
    """
    s= (a+b+c)/2 #semi-perimeter
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area(3,4,5))