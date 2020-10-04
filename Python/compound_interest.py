def simple_interest(principle, rate, time, number):
    '''
    Calculates compound interest where:
    1. principle is the amount of money.
    2. rate is the percentage.
    3. time for time period(in years).
    4. number is the number of terms in a year.
    '''
    ci = principle ( 1 + rate/(100*number))^(number*time)
    return ci
