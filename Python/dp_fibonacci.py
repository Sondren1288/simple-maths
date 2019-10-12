def dp_fibonacci(num):
    '''
    Returns fibonacci number of a given integer
    using dynamic programming for faster runtime

    Runtime: O(n)
    '''
    # Returns -1 if num is negative
    if num < 0:
        return -1
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    dp = [1,1]
    for i in range(2,num):
        dp.append(dp[i-1]+dp[i-2])

    return dp[-1]
