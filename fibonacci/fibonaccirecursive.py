def fibonac(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonac(n-1)+fibonac(n-2)


n = 9
print(fibonac(n))
