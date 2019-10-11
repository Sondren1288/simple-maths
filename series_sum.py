def var_sum(*args):
    """
    Variable argument sum
    """
    total = 0
    for arg in args:
        try:
            arg+1
            total += arg
        except TypeError: # invlid input hence return early
            return
    return total

def sum_of_n_natual_numbers(n):
    """
    Returns sum of first n natural numbers
    """
    try:
        n+1
    except TypeError: # invlid input hence return early
        return 
    if n < 1: # invlid input hence return early
        return 

    return n*(n+1) // 2

def sum_of_n_even_numbers(n):
    """
    Returns sum of first n even numbers
    """
    try:
        n+1
    except TypeError: # invlid input hence return early
        return 
    if n < 0: # invlid input hence return early
        return 

    return n*(n+1)

def sum_of_n_odd_numbers(n):
    """
    Returns sum of first n odd numbers
    """
    try:
        n+1
    except TypeError: # invlid input hence return early
        return 
    if n < 0: # invlid input hence return early
        return 

    return n*n

def sum_of_square_of_n_numbers(n):
    """
    The sum of squares of first n natural numbers
    ∑ n^2 = 1^2 + 2^2 + 3^2 +....+ n^2
    """
    try:
        n+1
    except TypeError: # invlid input hence return early
        return 
    if n < 0: # invlid input hence return early
        return 

    return n*(n+1)*(2*n+1)//6
