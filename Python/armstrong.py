def armstrong_number(number):
    """
    Check if number is Armstrong number
    """
    calc = number
    sum_ = 0
    while calc > 0:
        dig = calc % 10
        sum_ += dig ** 3
        calc //= 10
    if number == sum_:
        return True
    else:
        return False
