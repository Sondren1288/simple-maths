import math


def taylor_arctg(x, accuracy=20): 
    """
    A function to get arctg.
    It uses the taylor expansion.
    Check sine on wikipedia for better explanation.
    Be aware that this loses accuracy fairly quickly.
    Accuracy can be somewhat increased, but there is a limit
    to how large integers can be turned to floats.
    """
    multiplier = 1
    result = 0
    
    for i in range(1, accuracy, 2):
        result += multiplier * math.pow(x, i) / i
        multiplier *= -1
    
    return result
