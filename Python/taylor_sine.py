def getsin(x): 
    """
    A function to get sine of an angle in radians.
    It uses the taylor expansion of sine to calculate sine.
    Check sine on wikipedia for better explanation.
    """
    multiplier = 1
    result = 0
    
    for i in range(1,20,2):
        result += multiplier*pow(x,i)/math.factorial(i)
        multiplier *= -1
    
    return result
