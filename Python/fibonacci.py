def fibonacci_recursive(n):
    """
    To find the n-th number of a fibonacci sequence
    Starts with 0, 1, 1, 2
    """
    if n < 0:  # if invalid
        print("Invalid input")
    elif n == 1:  # base case n = 1, return 0
        return 0
    elif n == 2:  # base case if 2 then return 1
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)  # recursive


def fibonacci_recursive_cached(n, _cache={}):
    """
    Efficiently memoized recursive function, returns a Fibonacci number
    Starts with 1, 1, 2
    """
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, fibonacci_recursive_cached(n-1) + fibonacci_recursive_cached(n-2))
    return n


def fibonacci_dynamic(n):
    """
    Dynamic programming using bottom up approach for finding
    nth fibonacci Number in efficient time
    """
    if n == 1 or n == 2:
        return 1
    b_up = [None]*40
    b_up[0] = 0
    b_up[1] = 1
    b_up[2] = 2
    for i in range(2, n+1):
        b_up[i] = b_up[i-1] + b_up[i-2]
    return b_up[n]
