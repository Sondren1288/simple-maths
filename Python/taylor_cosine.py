import math


def taylor_cosine(x, accuracy=20): 
    """
    A function to get cosine of an angle in radians.
    It uses the taylor expansion of cosine to calculate cosine.
    Check cosine on wikipedia for better explanation.
    ## https://en.wikipedia.org/wiki/Trigonometric_functions#cos ##
    
    Be aware that this loses accuracy fairly quickly.
    Accuracy can be somewhat increased, but there is a limit
    to how large integers can be turned to floats.
    
    cosine(x) = 1 - x^2/2! + x^4/4! - x^6/6! ..  
    """
    multiplier = 1
    result = 0
    
    for i in range(0, accuracy, 2):
        result += multiplier * math.pow(x, i) / math.factorial(i)
        multiplier *= -1
    return result
