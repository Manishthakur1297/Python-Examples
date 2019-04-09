for t in range(int(input())):
    n = int(input())
    b = list(map(int,input().split())
    dp = (0,0)
    for i in range(1,n):
        dp = (max(dp[0],dp[1]+b[i-1]-1), max(dp[0]+b[i]-1, dp[1]+abs(b[i]-b[i-1])))
    print (max(dp))