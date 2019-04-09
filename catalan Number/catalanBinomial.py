def binomialCoefficient(n, k):
    if (k > n - k):
        k = n - k
    res = 1
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return res

def catalan(n):
    c = binomialCoefficient(2*n, n)
    return c/(n + 1)

n = 5000
arr = []
for i in range(n):
    arr.append(catalan(i))
print(arr)

