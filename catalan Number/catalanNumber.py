def catalanSeries(n):
    if n<=1:
        return 1
    res = 0
    for i in range(n):
        res+=catalanSeries(i) * catalanSeries(n-i-1)
    return res

n = 10
arr = []
for i in range(n):
    arr.append(catalanSeries(i))
print(arr)
