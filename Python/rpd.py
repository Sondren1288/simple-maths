def relatice_percent_difference(x,y):
    """
    Calculates the relative percent difference of 2 numbers 
    |x-y|/avg(x,y) * 100
    """
    average = abs(x + y) / 2
    rpd = abs(x - y) / average * 100
    return rpd 
