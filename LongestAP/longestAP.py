def LongestAP(arr):
    n = len(arr)
    dp = [1]*(n+1)
    ln = 1
    diff = arr[1]-arr[0]



arr = tuple(map(int,input().split(' ')))
print(LongestAP(arr))
