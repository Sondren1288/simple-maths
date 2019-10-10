def zeros(dimensions):
    """
    Attempted clone of numpy zeros.
    Not as quick, but might be useful if long lists are desired
    and numpy not available.
    """
    x = y = None
    try:
        y, x = dimensions  # If it cannot unpack it as tuple, it will fail
    except TypeError:
        x = dimensions  # If it fails, it will standard to 1 row
        y = 1

    zeros = []
    if y == 1:
        zeros += [0] * x
    else:
        for row in range(y):  # Makes rows with columns of 0
            zeros.append([0] * x)

    return zeros
