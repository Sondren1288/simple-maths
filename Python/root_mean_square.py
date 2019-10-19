import math

def rms(list_):
    """
    Finds the root mean square of a list of numbers
    """

    result = 0
    for num in list_:
        result += num*num
	
    result = result / len(list_)
    result = math.sqrt(result)
    return result
