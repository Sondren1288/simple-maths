def simple_interest(principle, rate, time):
    '''
    Calculates simple interest where:
    1. principle is the amount of money on which simple interest is to be calculated.
    2. rate is the percentage at which the simple interest is to be calculated.
    3. time for time period(in years) for which  simple interest is to be calculated
    '''
    si = (principle * rate * time) / 100
    return si
