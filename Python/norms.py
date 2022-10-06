def l1_norm(lst):
    """
    Calculates the l1 norm of a list of numbers
    """
    return sum([abs(x) for x in lst])

def l2_norm(lst):
    """
    Calculates the l2 norm of a list of numbers
    """
    return sum([x*x for x in lst])
    
def linf_norm(lst):
    """
    Calculates the l_infinity norm of a list of numbers
    """
    return max([abs(x) for x in lst])
