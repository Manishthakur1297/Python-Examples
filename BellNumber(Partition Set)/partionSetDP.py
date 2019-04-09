def partition(n,k):
    dp = [[0 for j in range(k+1)] for i in range(n+1)]
    #print(dp[1][1])
    for i in range(0,n+1):
        dp[i][0] = 0
    for i in range(0,k+1):
        dp[0][i] = 0

    for i in range(1,n+1):
        for j in range(1,k+1):
            if j==1 or j==i:
                dp[i][j] = 1
            else:
                dp[i][j] = j*dp[i-1][j] + dp[i-1][j-1]
    return dp[n][k]

print(partition(10,2))
