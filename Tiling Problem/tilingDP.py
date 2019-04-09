def tiling(n,m):
    tile = [0]*(n+2)

    for i in range(1,n+1):
        if i<m:
            tile[i] = 1
        elif i==m:
            tile[i] = 2
        else:
            tile[i]  = tile[i-1] + tile[i-m]
    return tile[n]


n = 7
m = 4
print(tiling(n,m))


