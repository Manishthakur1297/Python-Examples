t = int(input())
for i in range(t):
    n,m = map(int,input().split(' '))
    
    if(n%2==0):
        a = int(n/2)
        print(a*m)
    else:
        a = int(int(n/2) + 1)
        print(a*m)