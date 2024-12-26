def countWays(n) :
    # handle the base cases
    if n == 1 :
        return 1 
    elif n == 2 :
        return 2
    # create a dp array 
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    # Fill the dp array 
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print(countWays(5))
    