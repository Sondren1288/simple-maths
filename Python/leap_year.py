def is_leap (year):
    """
    Checks whether a year is a leap-year or not.
    IF the year is divisible by 4 it is a leap year, 
    unless it is divisible by 100, unless it is also divisible 
    by 400. 
    2000 = leap-year: divisible by 4, 100, and 400 - 400 makes it leap
    1900 = non-leap : divisible by 4, 100, not 400
    2004 = leap-year: divisible by 4, not 100 or 400
    """
    leap = False
    if year % 4 == 0 :
        leap = True
    if year % 100 == 0 and year % 400 != 0 :
        leap = False

    return leap
