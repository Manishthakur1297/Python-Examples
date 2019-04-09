#i = 0
def chordCount(n):
    #global i
    if n<=2:
        return n
    else:
        # i+=1
        # for j in range(0,n-1):
        #
        # return chordCount(i)*chordCount(n-i-1)

        dp = [1]*(n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            count = 0
            for j in range(i):
                mul = dp[j]*dp[i-j-1]
                count+=mul
            dp[i] = count
        print(dp)
        return dp[n]

n = int(input())
points = 2*n
print(chordCount(n))
