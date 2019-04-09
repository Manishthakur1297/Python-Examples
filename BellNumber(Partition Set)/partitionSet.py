def partition(n,k):
    if n==0 or k==0 or k>n:
        return 0
    elif k==n or k==1:
        return 1
    else:
        return k*partition(n-1,k) + partition(n-1,k-1)


print(partition(5,2))
