def rpd(x,y):
    """
    Calculates the relative percent difference of 2 numbers 
    |x-y|/avg(x,y) * 100
    """
    #x= float(x)
    #y= float(y)
    return abs(float(x-y))/abs(float((x+y)/2))*100
