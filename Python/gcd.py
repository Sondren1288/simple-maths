def gcd(n1, n2):
    """
    Non-Recursive function to return the GCD of n1 and n2
    """
    if n1 < n2:
		n1, n2 = n2, n1
	while n1 % n2:
		n1, n2 = n2, n1 % n2
	return n2
