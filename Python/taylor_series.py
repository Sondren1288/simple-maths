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
    
    for i in range(1, accuracy, 2):
        result += multiplier * math.pow(x, i) / math.factorial(i)
        multiplier *= -1
    
    return result


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
