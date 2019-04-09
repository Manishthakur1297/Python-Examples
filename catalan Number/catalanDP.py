def catalan(n):
    cat = [0]*(n+1)

    if n<=1:
        return 1
    else:
        cat[0] = 1
        cat[1] = 1
        for i in range(2,n+1):
            cat[i] = 0
            for j in range(i):
                cat[i] += cat[j]*cat[i-j-1]
        print(cat)
        return cat[n]


n = 50
arr = []
for i in range(n):
    arr.append(catalan(i))
print(arr)
