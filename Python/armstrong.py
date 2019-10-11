def armstrong_number(number):
    """
    Check if number is Armstrong number
    """
    calc = number
    sum = 0
    while calc > 0:
        dig = calc % 10
        sum += dig ** 3
        calc //= 10
    if number == sum:
        return True
    else:
        return False
    
