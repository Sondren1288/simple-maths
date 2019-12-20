def lcm(a,b):
    """
    Finds the least common multiple of 
    2 numbers without using GCD
    """
    greater = b if a < b else a
    while(True):
        if ((greater % a == 0) & (greater % b == 0)):
            lcm=greater
            break
        greater+=1
    return lcm

