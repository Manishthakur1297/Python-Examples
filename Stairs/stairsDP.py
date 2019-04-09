# def stairs(n):
#     if n<=2:
#         return n
#     else:
#         return stairs(n-1) + stairs(n-2)

def climbStairs(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


n = int(input())
print(climbStairs(n))
