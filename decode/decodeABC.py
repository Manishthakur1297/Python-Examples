def decode(l,n):
        # dp = [1]*(n)
        #
        # if l[0] == '0':
        #     return 0
        # for i in range(n):
        #     elem = int(l[i])
        #     if elem==0:
        #         dp = [0]*(n+1)
        #         break
        #
        # print('dp1 = ',dp)
        # if l[-1] == '0':
        #     dp[n-1] = 0
        # else:
        #     dp[n-1] = 1
        # for i in range(n-2,-1,-1):
        #     elem = int(str(l[i] + l[i+1]))
        #
        #     if elem<=26:
        #         if l[i]=='0':
        #             dp[i] = dp[i+1]
        #         else:
        #             dp[i] = dp[i+1]+1
        #     else:
        #         if l[i+1]=='0':
        #             return 0
        #         dp[i] = dp[i+1]
        # print('dp2 = ',dp)
        # return dp[0]

        x=[0]*(n+1);
        x[0]=1;
        x[1]=1
        if(l[0]=='0'):
            return 0
        print('dp1 = ',x)
        for i in range(1,n):
            if(int(l[i-1]+l[i])<=26 and int(l[i-1]+l[i])>0):
                f=1
            else:
                f=0
            if(l[i]=='0'):
                x[i+1]=x[i-1]*f
                if(x[i+1]==0):
                    x[n]=0
                    break
                x[i]=0
            else:
                x[i+1]=x[i]+x[i-1]*f
        print('dp2 = ',x)
        return x[n]


# 875361268549483279131
# 2611055971756562

l = list(input())
n = len(l)
print(decode(l,n))
