def bellNumber(n):
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    dp[0][0] = 1

    for i in range(1,n+1):
        dp[i][0] = dp[i-1][i-1]
        for j in range(1,i+1):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    return dp[n][0]

print(bellNumber(3))
