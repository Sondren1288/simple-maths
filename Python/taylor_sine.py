import math


def taylor_sine(x, accuracy=20): 
    """
    A function to get sine of an angle in radians.
    It uses the taylor expansion of sine to calculate sine.
    Check sine on wikipedia for better explanation.

    Be aware that this loses accuracy fairly quickly.
    Accuracy can be somewhat increased, but there is a limit
    to how large integers can be turned to floats.
    """
    multiplier = 1
    result = 0
    
    for i in range(1,accuracy,2):
        result += multiplier*math.pow(x,i)/math.factorial(i)
        multiplier *= -1
    
    return result
