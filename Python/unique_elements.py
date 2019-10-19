import collections


def unique_elements(list_):
    """
    Functions to find unique elements from a list of given numbers.
    Can also use 'list(set([list_]))'
    """
    uniques = []
    for number in list_:
        if number not in uniques:
            uniques.append(number)
    
    return uniques


def frequency(list_):
    """
    Finds the occurances of elements in a list.
    Works with numbers not consisting of numbers as well
    """
    occurances = collections.Counter(list_)
    return occurances
    
