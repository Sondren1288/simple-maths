'''

Fibonacci:
n = (n-1)+(n-2)

N-nacci:
n = (n-m)+(n-m-1)

eg.:
Fibonacci(4):
4 = (4-1)+(4-2) = 5

N-nacci(11,10)
11 = (11-10) + (11-10-1) = 1

'''

def n_nacci(n, m):
    if (n-m)+(n-m-1) <= 0:
        raise SystemError("Invalid parameters")
    else:
        return (n-m)+(n-m-1)

cli = False
if cli == True:
    import sys
    n = sys.argv[1]
    m = sys.argv[2]
    n_nacci(n,m)
else:
    pass