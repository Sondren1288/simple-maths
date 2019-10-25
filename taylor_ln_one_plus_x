import math


def taylor_ln_one_plus_x(x, accuracy=20): 
    """
    A function to get ln(1+x).
    It uses the taylor expansion.
    Check sine on wikipedia for better explanation.
    Be aware that this loses accuracy fairly quickly.
    Accuracy can be somewhat increased, but there is a limit
    to how large integers can be turned to floats.
    """
    multiplier = 1
    result = 0
    
    for i in range(1, accuracy, 1):
        result += multiplier * math.pow(x, i) / i
        multiplier *= -1
    
    return result
