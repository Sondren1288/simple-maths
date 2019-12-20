import math


def taylor_exp(x, accuracy=20): 
    """
    A function to get e^x.
    It uses the taylor expansion of e^x.
    ## https://en.wikipedia.org/wiki/Exponential_function ##
    
    Be aware that this loses accuracy fairly quickly.
    Accuracy can be somewhat increased, but there is a limit
    to how large integers can be turned to floats.
    
    e^x = 1 + x + x^2/2! + x^3/3! + x^4/4!...
    """
    result = 0
    
    for i in range(0, accuracy, 1):
        result += math.pow(x, i) / math.factorial(i)
    
    return result
