import math


def taylor_arctan(x, accuracy=20): 
    """
    A function to get arctan.
    It uses the taylor expansion.
    Check arctan on wikipedia for better explanation.
    ## https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#arctan ##
    
    Be aware that this loses accuracy fairly quickly.
    Accuracy can be somewhat increased, but there is a limit
    to how large integers can be turned to floats.
    
    arctan(x) = x - x^3/3 + x^5/5 - x^7/7...
    """
    multiplier = 1
    result = 0
    
    for i in range(1, accuracy, 2):
        result += multiplier * math.pow(x, i) / i
        multiplier *= -1
    
    return result
