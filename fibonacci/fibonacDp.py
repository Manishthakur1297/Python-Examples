def fibonac(n):
    fibon = [0]*(n+1)
    fibon[0] = 0
    fibon[1] = 1
    if n<=1:
        return fibon[n]
    for i in range(2,n+1):
        fibon[i] = fibon[i-1]+fibon[i-2]
    return fibon[n]


n = 9
print(fibonac(n))
