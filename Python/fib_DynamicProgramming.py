
#DYNAMIC PROGRAAMING USING BOTTOM UP APPROACH FOR FINDING nth fibonacci Number in efficient time
def fib(n):
    if n==1  or n==2:
        return 1
    b_up=[None]*40
    b_up[0]=0
    b_up[1]=1
    b_up[2]=2
    for i in range(2,n+1):
        b_up[i]=b_up[i-1]+b_up[i-2]
    return b_up[n]



