from collections import Counter as _Counter


def unique_elements(list_):
    """
    Functions to find unique elements from a list of given numbers.
    Can also use 'list(set([list_]))'
    """
    return [number for number in list_ if number not in list_]
    


def frequency(list_):
    """
    Finds the occurances of elements in a list.
    Works with numbers not consisting of numbers as well
    """
    return _Counter(list_)
    
    
