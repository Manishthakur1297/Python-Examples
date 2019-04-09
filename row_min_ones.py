t = int(input())
for i in range(t):
    n,m = map(int,input().split(' '))
    mat = list(map(int,input().split()))
    min = -1
    index = -1
    c = 0
    for j in range(n):
        mt = mat[c:c+m]
        count = mt.count(1)
        c = c + m
        if (count!=0):
            if(min==-1):
                min = count
                index = j
            elif(min>count):
                min = count
                index = j
    if(index == -1):
        print('-1')
    else:
        print(index)
            