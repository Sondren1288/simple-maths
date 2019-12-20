import math


def ln_one_plus_x(x, accuracy=20): 
    """
    A function to get ln(1+x).
    It uses the taylor expansion.
    Check natural logarithm on wikipedia for better explanation.
    ## https://en.wikipedia.org/wiki/Natural_logarithm ##
    Be aware that this loses accuracy fairly quickly.
    Accuracy can be somewhat increased, but there is a limit
    to how large integers can be turned to floats.
    ln(1 + x) = x - x^2/2 + x^3/3 - x^4/4...
    """
    multiplier = 1
    result = 0
    
    for i in range(1, accuracy, 1):
        result += multiplier * math.pow(x, i) / i
        multiplier *= -1
    
    return result
