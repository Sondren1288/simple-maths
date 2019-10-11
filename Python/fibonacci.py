#Recursive Function to get the Fibonacci-Sequence of a given Number n.
#

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
