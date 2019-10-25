import math


def taylor_exp(x, accuracy=20): 
    """
    A function to get e^x.
    It uses the taylor expansion.
    Be aware that this loses accuracy fairly quickly.
    Accuracy can be somewhat increased, but there is a limit
    to how large integers can be turned to floats.
    """
    result = 0
    
    for i in range(0, accuracy, 2):
        result += math.pow(x, i) / math.factorial(i)
    
    return result
