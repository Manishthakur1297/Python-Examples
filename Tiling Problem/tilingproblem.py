def tiling(n):
    if n==1 or n==2:
        return n
    else:
        return tiling(n-1)+tiling(n-2)


print(tiling(4))
